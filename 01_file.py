#현재 작업 중인 디렉터리 확인
import os
current_directory = os.getcwd() #현재 작업 절대 경로
##os 모듈 : 파일들을 담당하는 모듈
print("Current working directory:", current_directory)

file_path = "file.txt"

#모듈os의 클래스path : 파일에 대한 접근시간, 변경시간, 사이즈 등(getatime, getmtime, getsize)
#isfile 파일임을 검사    
if os.path.isfile(file_path):
    print(f"{file_path}는 파일이다!")
else:
    print(f"{file_path}는 파일이 아니다!!")

#isdir 디렉터리 임을 검사
if os.path.isdir(file_path):
    print(f"{file_path}는 디렉터리다!")
else:
    print(f"{file_path}는 디렉터리가 아니다!!")
    