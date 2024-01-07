import tensorflow as tf
from PIL import Image
import os
import time
import numpy as np
import glob
import xml.etree.ElementTree as ET
from object_detection.utils import dataset_util
from object_detection.utils import label_map_util


def create_tfrecord(image_folder, label_map_dict, output_path):
    # TFRecordWriter 생성
    writer = tf.io.TFRecordWriter(output_path)
    print("TFRecordWriter 생성...")

    print("이미지 파일 이름 추출 시작...")
    # 이미지 파일 이름 추출
    image_filename2='0'
    image_filenames = os.listdir(image_folder)
    # 이미지 파일에 대해 작업 수행
    for filename in image_filenames:
        if filename.endswith('.jpg'):
            #Object 수 확인을 위해 파일이름 비교
            if filename != image_filename2:
                Object_Count=1
                image_filename2=filename
            print("파일 이름 :", filename)
            # 이미지 파일 경로
            image_path = os.path.join(image_folder, filename)
            # 이미지 로드
            image = Image.open(image_path)
            # 이미지 크기
            width = image.width
            height = image.height

            # 객체 정보 추출
            objects = []
            # 파싱
            # 해당 이미지의 객체 정보 추출
            for box in root.findall(f'image[@name="{os.path.basename(image_path)}"]/box'):
                label = box.get('label')
                occluded = int(box.get('occluded'))
                xtl = float(box.get('xtl'))
                ytl = float(box.get('ytl'))
                xbr = float(box.get('xbr'))
                ybr = float(box.get('ybr'))
                z_order = int(box.get('z_order'))

                # 객체 정보를 딕셔너리로 저장
                info = {
                    'file': filename,
                    'class_label': label,
                    'bbox': [xtl, ytl, xbr, ybr],
                    'occluded': occluded,
                    'z_order': z_order
                }
                objects.append(info)

            # 이미지와 객체 정보를 데이터셋에 추가
            #dataset = []
            #dataset.append({'image': image, 'objects': objects})

            # 바운딩 박스 정보 및 클래스 매핑
            bboxes = []
            class_labels = []
            # 이미지의 객체 정보를 바운딩 박스와 클래스로 분리하여 저장
            for obj in objects:
                bbox = obj['bbox']
                class_label = obj['class_label']
                # 바운딩 박스 정보 추가
                bboxes.append(bbox)
                # 클래스 정보 추가
                class_labels.append(class_label)
            
            print("객체 정보를 분리 하였습니다.")                
            # bboxes와 classes 리스트의 길이 확인
            if len(bboxes) != len(class_labels):
                print("Error: '바운딩박스'와 'classes'의 길이가 일치하지 않습니다!")
                exit()
            # 클래스의 개수 확인
            num_classes = len(label_map_dict)
            if len(set(class_labels)) > num_classes:
                print("Error: 클래스의 수가 정의된 클래스의 수를 초과합니다!")
                exit()            
            '''except (FileNotFoundError, UnidentifiedImageError):
                # 이미지 파일 로드 실패 시 예외 처리
                # ...
                pass'''

            # 이미지 배열
            image_np = np.array(image)
            # 파싱
            # ...
            
            print("객체 정보 TFRecord 변환 시작...")
            Object_Count = 1
            # 객체 정보를 사용하여 TFRecord 형식으로 변환 및 저장
            for i in range(len(bboxes)):
                xmin, ymin, xmax, ymax = bboxes[i]
                class_label = class_labels[i]
                class_id = label_map_dict[class_label]

                # 바운딩 박스 정보
                xmins = [xmin / width]
                ymins = [ymin / height]
                xmaxs = [xmax / width]
                ymaxs = [ymax / height]
                classes_text = [class_label.encode('utf8')]
                classes = [class_id]
                num_objects = len(bboxes)

                # TFRecord 형식으로 변환
                tf_example = tf.train.Example(features=tf.train.Features(feature={
                    'num_objects': dataset_util.int64_feature(num_objects),
                    'image/height': dataset_util.int64_feature(height),
                    'image/width': dataset_util.int64_feature(width),
                    'image/filename': dataset_util.bytes_feature(filename.encode('utf8')),
                    'image/source_id': dataset_util.bytes_feature(filename.encode('utf8')),
                    'image/encoded': dataset_util.bytes_feature(image_np.tobytes()),
                    'image/format': dataset_util.bytes_feature('jpeg'.encode('utf8')),
                    'image/object/bbox/Object_Count': dataset_util.int64_feature(Object_Count),
                    'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
                    'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
                    'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
                    'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
                    'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
                    'image/object/class/label': dataset_util.int64_list_feature(classes),
                }))

                #TFRecordWriter에 작성
                writer.write(tf_example.SerializeToString())
                Object_Count += 1
            print("객체 정보 TFRecord 변환 완료.\n\n")

    # TFRecordWriter 닫기
    writer.close()
    print("TFRecord 파일 생성 완료.")
    return

'''def parse_tfrecord_fn(example, desired_label):

        # TFRecord 데이터 파싱 로직 작성
    feature_description = {
        'image/height': tf.io.FixedLenFeature([], tf.int64),
        'image/width': tf.io.FixedLenFeature([], tf.int64),
        'image/filename': tf.io.FixedLenFeature([], tf.string),
        'image/source_id': tf.io.FixedLenFeature([], tf.string),
        'image/encoded': tf.io.FixedLenFeature([], tf.string),
        'image/format': tf.io.FixedLenFeature([], tf.string),
        'image/object/bbox/xmin': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/xmax': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/ymin': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/ymax': tf.io.VarLenFeature(tf.float32),
        'image/object/class/text': tf.io.VarLenFeature(tf.string),
        'image/object/class/label': tf.io.VarLenFeature(tf.int64),
    }

    example = tf.io.parse_single_example(example, feature_description)
    indices = tf.where(tf.equal(tf.sparse.to_dense(example['image/object/class/text']), desired_label))
    
    if tf.shape(indices)[0] > 0:
        xmin = tf.gather(tf.sparse.to_dense(example['image/object/bbox/xmin']), indices)
        xmax = tf.gather(tf.sparse.to_dense(example['image/object/bbox/xmax']), indices)
        ymin = tf.gather(tf.sparse.to_dense(example['image/object/bbox/ymin']), indices)
        ymax = tf.gather(tf.sparse.to_dense(example['image/object/bbox/ymax']), indices)
        
        parsed_data = {
            'xmin': xmin,
            'xmax': xmax,
            'ymin': ymin,
            'ymax': ymax
        }
    else:
        parsed_data = {
            'xmin': tf.constant([]),
            'xmax': tf.constant([]),
            'ymin': tf.constant([]),
            'ymax': tf.constant([])
        }
        
    return parsed_data
    '''

def parse_tfrecord_fn(example):
    # TFRecord 데이터 파싱 로직 작성
    feature_description = {
        'image/height': tf.io.FixedLenFeature([], tf.int64),
        'image/width': tf.io.FixedLenFeature([], tf.int64),
        'image/filename': tf.io.FixedLenFeature([], tf.string),
        'image/source_id': tf.io.FixedLenFeature([], tf.string),
        'image/encoded': tf.io.FixedLenFeature([], tf.string),
        'image/format': tf.io.FixedLenFeature([], tf.string),
        'image/object/bbox/Object_Count': tf.io.VarLenFeature(tf.int64),
        'image/object/bbox/xmin': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/xmax': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/ymin': tf.io.VarLenFeature(tf.float32),
        'image/object/bbox/ymax': tf.io.VarLenFeature(tf.float32),
        'image/object/class/text': tf.io.VarLenFeature(tf.string),
        'image/object/class/label': tf.io.VarLenFeature(tf.int64),
    }

    example = tf.io.parse_single_example(example, feature_description)
    
    num_objects = tf.shape(example['image/object/bbox/xmin'])[0]
    Object_Count = tf.sparse.to_dense(example['image/object/bbox/Object_Count'])
    xmin = tf.sparse.to_dense(example['image/object/bbox/xmin'])
    xmax = tf.sparse.to_dense(example['image/object/bbox/xmax'])
    ymin = tf.sparse.to_dense(example['image/object/bbox/ymin'])
    ymax = tf.sparse.to_dense(example['image/object/bbox/ymax'])
    labels = tf.sparse.to_dense(example['image/object/class/text'], default_value='')

    return num_objects, xmin, xmax, ymin, ymax, labels, example, Object_Count

#XML 파일 로드
xml_file_path = 'bbox/bbox_sample.xml'  # XML 파일 경로로 대체

tree = ET.parse(xml_file_path)
root = tree.getroot()
print("XML파일 로드 완료.")
'''# XML 파일 내용 출력
print(ET.tostring(root, encoding='utf-8').decode('utf-8'))
XML 파일 라벨 이름 출력
for label in root.findall('./label/name'):
    label_name = label.text
    print("label name:", label_name)'''

# 이미지 파일이 들어있는 폴더 경로
image_folder = './bbox/'  # 실제 이미지 폴더의 경로로 수정해야 합니다.
print("이미지폴더 로드 완료.")
{# 폴더 내의 모든 이미지 파일 로드
'''
image_paths = []
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):  # 이미지 파일 형식에 따라 확장자를 수정해야 합니다.
        image_path = os.path.join(image_folder, filename)
        image_paths.append(image_path)'''

'''# 이미지 파일 이름 추출
image_filenames = []
for filename in os.listdir(image_folder):
    image_filenames.append(filename)
# 이미지 파일 이름 출력
for filename in image_filenames:
    print(filename)
        
# 이미지 파일 개수 출력
print('이미지 개수:', len(image_paths))'''

'''# 이미지와 객체 정보를 저장할 리스트
dataset = []
# 각 이미지 파일에 대해 작업 수행
for image_path in image_paths:
    # 이미지 파일 로드
    image = Image.open(image_path)
    width, height = image.size

    # 해당 이미지의 객체 정보 추출
    object_info = []
    for box in root.findall(f'image[@name="{os.path.basename(image_path)}"]/box'):
        label = box.get('label')
        occluded = int(box.get('occluded'))
        xtl = float(box.get('xtl'))
        ytl = float(box.get('ytl'))
        xbr = float(box.get('xbr'))
        ybr = float(box.get('ybr'))
        z_order = int(box.get('z_order'))

    # 객체 정보를 딕셔너리로 저장
    info = {
        'bbox': [xtl, ytl, xbr, ybr],
        'class_label': label,
        'occluded': occluded,
        'z_order': z_order
    }
    object_info.append(info)

    # 이미지와 객체 정보를 데이터셋에 추가
    dataset.append({'image': image, 'objects': object_info})'''

'''
# 학습 결과를 txt 파일에 저장
with open(output_file, 'w') as f:
    # 학습 결과를 데이터셋 순서대로 저장
    for i, data in enumerate(dataset):
        image = data['image']  # 이미지
        objects = data['objects']  # 객체 정보

        # 이미지 파일명과 해당 이미지에 대한 학습 결과를 저장
        f.write(f'Image {i+1}: {image}\n')
        
        # 객체 정보와 해당 객체에 대한 학습 결과를 저장
        for j, obj in enumerate(objects):
            bbox = obj['bbox']  # 객체의 바운딩 박스 좌표
            class_label = obj['class_label']  # 객체의 클래스 레이블
            
            # 객체 정보와 학습 결과를 저장
            f.write(f'  Object {j+1}: {bbox}, Class Label: {class_label}\n')
        f.write('\n')  # 다음 데이터셋을 위한 줄바꿈

print("학습 결과를 training_results.txt에 저장완료!")'''
}

# 라벨 맵 딕셔너리
label_map_dict = {}
# 모든 이미지 요소에 대해 반복
for image in root.findall('image'):
    # 모든 박스 요소에 대해 반복
    for box in image.findall('box'):
        class_label = box.get('label')
        class_id = label_map_dict.get(class_label)
        if class_id is None:
            # 새로운 클래스 레이블이라면 클래스 ID를 할당하여 매핑
            class_id = len(label_map_dict) + 1
            label_map_dict[class_label] = class_id
#라벨 맵 딕셔너리 출력
#print(label_map_dict)


# 데이터셋 활용하여 학습을 수행
# 학습이 완료되었다고 가정하고, 학습 결과를 저장할 파일 경로
output_file = 'tensorflow_Output/train.tfrecord'
print("tensorflow_Output/train.tfrecord 경로 지정 완료.")

# XML파일과 이미지 파일을 로드하여 원하는 작업 수행
#create_tfrecord(image_folder, label_map_dict, output_file)

# TFRecord 파일 경로 가져오기
tfrecord_files = glob.glob(output_file)
# TFRecordDataset 생성
dataset = tf.data.TFRecordDataset(tfrecord_files)
print("TFRecordDataset 파일 생성 완료")


# 원하는 라벨 설정
'''desired_label = "person"
# TFRecord 데이터 파싱 적용
parsed_dataset = dataset.map(lambda x: parse_tfrecord_fn(x, desired_label))
parsed_dataset = parsed_dataset.repeat()
#반환되는 요소 개수 확인
print(parsed_dataset.element_spec)

# # 데이터 사용 예시
# for image, label in parsed_dataset:
#     # 이미지와 레이블에 대한 원하는 작업 수행
#     # 예: 모델 입력으로 사용 또는 이미지 시각화 등
#     pass
# 파싱된 데이터 확인
for example in parsed_dataset:
    # print("찾는 중---")
    if example['xmin'].shape[0] > 0:
        xmin = tf.squeeze(example['xmin']).numpy()
        xmax = tf.squeeze(example['xmax']).numpy()
        ymin = tf.squeeze(example['ymin']).numpy()
        ymax = tf.squeeze(example['ymax']).numpy()
        print("label:", desired_label)
        print("xmin:", xmin ,
              "ymin:", ymin,
              "xmax:", xmax,
              "ymax:", ymax,)
        # 시간지연
        # time.sleep(0.3)'''

# TFRecord 데이터 파싱 적용
parsed_dataset = dataset.map(parse_tfrecord_fn)

# 파싱된 데이터 확인
for num_objects, xmin, xmax, ymin, ymax, labels, example ,Object_Count in parsed_dataset:
    image_filename = example['image/filename'].numpy().decode()
    print("Image Filename:", image_filename)
    print("Object: ", Object_Count.numpy())
    for i in range(num_objects):
        print("label:", labels[i].numpy().decode())
        print("xmin:", xmin[i].numpy())
        print("xmax:", xmax[i].numpy())
        print("ymin:", ymin[i].numpy())
        print("ymax:", ymax[i].numpy())
    print("-" * 20)
    # 시간지연
    # time.sleep(0.4)