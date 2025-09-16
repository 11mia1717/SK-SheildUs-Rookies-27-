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


# 기능 추가 - txt파일들의 내용을 출력해보세요!!


#filename을 가져와서 읽어오려고 하면 오류가 발생
#왜냐면 filepath를 잡아줘야하기때문
#uploads라는 하위 디렉터리에 있어서 경로 설정해줘야함.

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    print(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"{filename} 내용 : \n")
        print(file.read())
        print("="*40)





"""
잘안된다 ㅠ
for i in range(len(txt_files)):
    with open(txt_files[i], 'r', encoding='utf-8') as txtFile:
    content = txtFile.read()
    print(content)
"""


# 기능 추가 01 - readlines() 읽어서 줄 단위로 검사!
# 기능 추가 02 - 파일 앞쪽에 # 나 // 주석처리 된 것을 찾아내시오 
# ㄴ startswith("#")을 활용
# 기능 추가 03 - 출력 예제는 "파일이름 : 1번째 라인 탐지 : 내용"

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    #print(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines() #readlines로 받아온 리스트값을 lines에 담는다.
        #print(lines)
        #라인별로 확인했을 때 
        #enumerate() = 인덱스 + 값 동시 반환
        #>반복 가능한 객체(list, tuple, string 등)를 순회할 때 인덱스(번호)와 요소를 함께 꺼내주는 내장 함수.
        for i, line in enumerate(lines): 
            if line.startswith("#") or line.startswith("//") or line.startswith("<--!"):
                print(f"{filename} {i+1}번째 라인 -> 탐지 : {line.strip()}")
                #strip. 이스케이프문자나 \n에 대해 처리를 해줌
                #문자열 양쪽(앞, 뒤)의 공백 문자(스페이스, 개행 \n, 탭 \t 등) 를 제거
        
        
        