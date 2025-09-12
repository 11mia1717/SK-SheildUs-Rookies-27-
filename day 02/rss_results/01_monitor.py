#파일 모니터링 기능
import os
import time
from datetime import datetime 
#datetime 라이브러리 안에 datetime의 클래스만 가져오겠다

dir_path = "uploads"
#pre_file = os.listdir(dir_path)
pre_file = set(os.listdir(dir_path)) #set으로 형변환
print(f"pre_file{pre_file}")
#pre_file = 탐지를 하기 전에 파일 목록 저장

      
while True: #무한으로 탐지!
     now = datetime.now() #현재시간
     day = now.strftime("%Y-%m-%d")
     hour = now.strftime("%H:%M:%S")
     
     #"%d/%m/%Y, %H:%M:%S"

     #current_file = os.listdir(dir_path)
     current_file = set(os.listdir(dir_path))
     result_diff = current_file - pre_file 
     # 리스트의 차이점을 보면 새로운 파일을 알 수 있을거야 --> 에러
     # 리스트들은 더하기가 가능하지만 빼기가 불가능 support 하지않음
     # 형변환을 시켜주자 set

     #print(f"current_file: {current_file}")
     print(f"파일 생성 : {result_diff}")

     #result_diff가 몇개일지모른다
     #탐지된 파일의 목록을 txt 파일에 저장
     for file_name in result_diff:
          with open(f"{day}_탐지_보고서.txt", "a", encoding="utf-8") as file :
               #"a"를 넣어 add 추가옵션
               file.write(f"작성자 : 장민아\n")
               file.write(f"탐지된 날짜 : {hour}\n")
               file.write(f"주요 내용 : 신규 파일 탐지\n")
               file.write(f"탐지된 파일 : {file_name}\n")
               file.write("===============\n")
            

     pre_file = current_file #현재 파일이 이전파일이니깐
     time.sleep(1) # 1초마다 탐지하게 함
     # exameple.txt 파일은 uploads폴더에 넣으면 
     # #current_file에만 포함되어 출력]