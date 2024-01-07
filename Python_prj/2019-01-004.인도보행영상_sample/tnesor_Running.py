import tensorflow as tf
from object_detection.utils import dataset_util
from object_detection.utils import label_map_util
from PIL import Image
import os
import numpy as np
import xml.etree.ElementTree as ET

#XML 파일 로드
xml_file_path = 'bbox/bbox_sample.xml'  # XML 파일 경로로 대체

# XML 파일 파싱
tree = ET.parse(xml_file_path)
root = tree.getroot()

# # 라벨과 클래스 ID를 매핑하는 딕셔너리
# label_map_dict = {}
# # 모든 label 요소에 대해 반복하여 클래스 레이블과 클래스 ID 매핑
# for label in root.findall('label'):
#     class_label = label.find('name').text
#     class_id = label_map_dict.get(class_label)
#     if class_id is None:
#         # 새로운 클래스 레이블이라면 클래스 ID를 할당하여 매핑
#         class_id = len(label_map_dict) + 1
#         label_map_dict[class_label] = class_id
# # label_map_dict 확인
# print(label_map_dict)

# # 객체 정보 추출
# object_info = []
# for box in root.findall('image/box'):
#     label = box.get('label')
#     xtl = float(box.get('xtl'))
#     ytl = float(box.get('ytl'))
#     xbr = float(box.get('xbr'))
#     ybr = float(box.get('ybr'))
#     z_order = int(box.get('z_order'))

#     # 객체 정보를 딕셔너리로 저장
#     info = {
#         'bbox': [xtl, ytl, xbr, ybr],
#         'class_label': label,
#         'class_id': label_map_dict[label]
#     }
#     object_info.append(info)


# # 이미지 파일이 들어있는 폴더 경로
# image_folder = './bbox/'  # 실제 이미지 폴더의 경로로 수정해야 합니다.

# # 폴더 내의 모든 이미지 파일 로드
# image_paths = []
# for filename in os.listdir(image_folder):
#     if filename.endswith('.jpg'):  # 이미지 파일 형식에 따라 확장자를 수정해야 합니다.
#         image_path = os.path.join(image_folder, filename)
#         image_paths.append(image_path)

# # 이미지 파일 이름 추출
# image_filenames = []
# for filename in os.listdir(image_folder):
#     image_filenames.append(filename)
# # 이미지 파일 이름 출력
# #for filename in image_filenames:
# #    print(filename)

# # 이미지 파일 개수 출력
# #print('이미지 개수:', len(image_paths))

# # 객체 정보를 사용하여 TFRecord 파일에 데이터를 저장하는 작업을 수행하세요.

# # 라벨 맵 파일 경로
# label_map_path = 'bbox/bbox_sample.xml'  # XML 파일 경로로 대체  # 라벨 맵 파일 경로로 대체해주세요.

# # TFRecord 파일 생성 함수
# def create_tf_example(image_path, label_map_dict):
#     # 이미지 로드
#     image = Image.open(image_path)
    
#     # 이미지 크기
#     width = image.width
#     height = image.height
    
#     # 이미지 배열
#     image_np = np.array(image)
    
#     # 이미지 파일 이름 추출
#     image_filename = os.path.basename(image_path)

#     # # 첫 번째 객체 정보를 가져옴
#     # object_info_0 = object_info[0]
#     # x_min, y_min, x_max, y_max = object_info_0['bbox']
#     # class_label = object_info_0['class_label']
#     # class_id = object_info_0['class_id']

#     for i in range(len(image_paths)):
#       object_info_0 = object_info[i]
#       x_min, y_min, x_max, y_max = object_info_0['bbox']
#       class_label = object_info_0['class_label']
#       class_id = object_info_0['class_id']
    
#     # 바운딩 박스 정보
#     xmins = [x_min / width]
#     ymins = [y_min / height]
#     xmaxs = [x_max / width]
#     ymaxs = [y_max / height]
#     classes_text = [class_label.encode('utf8')]
#     classes = [class_id]
    
#     # TFRecord 형식으로 변환
#     tf_example = tf.train.Example(features=tf.train.Features(feature={
#         'image/height': dataset_util.int64_feature(height),
#         'image/width': dataset_util.int64_feature(width),
#         'image/filename': dataset_util.bytes_feature(image_filename.encode('utf8')),
#         'image/source_id': dataset_util.bytes_feature(image_filename.encode('utf8')),
#         'image/encoded': dataset_util.bytes_feature(image_np.tobytes()),
#         'image/format': dataset_util.bytes_feature('jpeg'.encode('utf8')),
#         'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
#         'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
#         'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
#         'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
#         'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
#         'image/object/class/label': dataset_util.int64_list_feature(classes),
#     }))
    
#     return tf_example

# def main():
#     # 라벨 맵 로드
#     label_map_dict = label_map_util.get_label_map_dict(label_map_path)
    
#     # TFRecord 파일 저장 경로
#     output_path = 'tensorflow_Output/output.tfrecord'  # 저장할 경로 지정