import os
import re

dir_path = "uploads"
all_files = os.listdir(dir_path)
txt_files = []

for file in all_files:
    if file.endswith('.txt'):
        txt_files.append(file)

#디렉터리내의 txt 파일을 하나씩 불러와서 오픈
for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if line.startswith("#") or line.startswith("//"):
                print(f"주석 {file_path} {index+1}라인 : 탐지 {line}")

            #if re.search(r'\d{6}[-]\d{7}',line): #바로 적어도 되고
            #미리 컴파일 하고 적어도 됨. 큰 차이는 없음. 

            #공백포함 주민번호 서치
            if re.search(r'\d{6}\s*[-]\s*\d{7}',line): 
            #\s* : * 0개 이상 반복. 즉, 없어도 되고 있어도 되고.
                
                print(f"주민번호 {file_path} {index+1}라인 : 탐지 {line}")
