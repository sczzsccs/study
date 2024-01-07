import os
import random
import pandas as pd
import openpyxl
from openpyxl.drawing.image import Image

def get_col_width_row_height(img_width, img_height):
    col_width = img_width*63.2/504
    row_height = img_height*225/300
    return (col_width, row_height)

wb = openpyxl.load_workbook("./문제은행제작/문제은행.xlsx")
ws = wb.active ## 첫 번째 시트

# 폴더 경로
path = "./수학 문제"
File_Dict = {} # 모든 이미지 파일저장
Image_Count = 0

# 폴더 내 모든 이미지 파일 읽기
Stage_List = os.listdir(path)
# 단원 경로
for Stage in Stage_List:
    File_Dict[Stage] = {}
    Stage_path = path+'/'+Stage
    Level_List = os.listdir(Stage_path)
    # 난이도 경로
    for Level in Level_List:
        Level_path = Stage_path+'/'+Level
        Image_Path = os.listdir(Level_path)
        File_Dict[Stage][Level] = Image_Path
        Image_Count += len(Image_Path)

print(File_Dict)

def Try_Level_idx(level_list:list):
    try: level = level_list[0]
    except: 
        try: level = level_list[1]
        except: level = level_list[2]
    return level

for i in range(Image_Count):
    print(i, end=", ")
    path = "./수학 문제" # 폴더 경로 지정
    Rand_Stage = random.randrange(len(File_Dict))
    Rand_Stage = list(File_Dict.keys())[Rand_Stage]
    print(Rand_Stage, end=", ")

    Rand_Level = random.randrange(1, 11)

    level_list = list(File_Dict[Rand_Stage].keys())
    print(level_list)
    if Rand_Level >= 9:
        level = Try_Level_idx(level_list)
    if Rand_Level >=6:
        level = Try_Level_idx(level_list)
    else: 
        level = Try_Level_idx(level_list)

    Rand_Image = random.randrange(len(File_Dict[Rand_Stage][level]))

    print(level, end=", ")
    print(Rand_Image, end=", ")

    image_path = path+"/"+str(Rand_Stage)+"/"+level+'/'+File_Dict[Rand_Stage][level][Rand_Image]
    print("image_path:", image_path)
    image = Image(image_path) ## 이미지 로드

    # 중복방지 요소 삭제
    Level_List = list(File_Dict[Rand_Stage][level])
    Level_List.remove(File_Dict[Rand_Stage][level][Rand_Image])
    File_Dict[Rand_Stage][level] = Level_List
    if len(File_Dict[Rand_Stage][level]) == 0: del File_Dict[Rand_Stage][level]
    if len(File_Dict[Rand_Stage]) == 0: del File_Dict[Rand_Stage]
    print(File_Dict)

if i <= 7:
    ws.add_image(image, anchor='A' + str(1+i)) ## 이미지 삽입
    image.width = 260
    image.height = 200
else:
    ws.add_image(image, anchor='B' + str(1 + i%8)) ## 이미지 삽입
    image.width = 260
    image.height = 200

print(len(submitted))
print("결과:", submitted)
wb.save("./문제은행제작/문제은행.xlsx")