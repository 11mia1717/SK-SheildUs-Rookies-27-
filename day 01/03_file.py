#uploads폴더안에 파일을 뽑아내서 txt파일 확장자만 가져오기

import os
dir_path = "uploads"
all_files = os.listdir(dir_path)

#리스트 형태를 임시 저장용으로 사용
txt_files = [] 

for file in all_files:
    #endswith() 문자열이 특정 **접미사(suffix)**로 끝나는지 확인할 때 사용
    if file.endswith(".txt"):
        txt_files.append(file) #리스트 append 끝에 요소 추가

print(txt_files)

print("="*40)

