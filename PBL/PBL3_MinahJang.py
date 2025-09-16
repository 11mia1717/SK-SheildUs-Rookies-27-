#디렉토리 파일 감지 시스템 구축
#보안 담당자는 중요한 서버에 업로드 되는 파일에 
#개인정보가 포함되어있는지 여부를 모니터링 하고 싶다.
#외부에 중요 정보가 노출이 되기 전에 잠재적 보안 위협을 방지하고 싶어한다.

import os
import time
from datetime import datetime 

#특정 디렉토리 경로 지정
dir_path = "Security_Check"

#초기 디렉터리 안의 파일을 확인(pre_file), 리스트간 비교를 위해 형변환
pre_file = set(os.listdir(dir_path)) 
print(f"[log] 탐지 경로 확인했습니다 {dir_path}")
      
#시스템 보안파일 모니터링을 반복문으로 계속 탐지      
while True: 
     #현재 시간을 선언  
     now = datetime.now() 
     day = now.strftime("%Y-%m-%d")
     hour = now.strftime("%H:%M:%S")

     #특정 디렉터리에 있는 현재 파일 목록 확인
     current_file = set(os.listdir(dir_path))
     
     #파일 변경 사항을 확인(리스트간 비교)
     new_files = current_file - pre_file 
     
     #신규 탐지된 파일 리스트 확인
     if new_files :
         file_list=", ".join(new_files)
         print(f"[detect] 탐지날짜:{day} {hour}, 탐지된 신규 파일명 : {file_list}")

     #삭제된 파일 리스트 확인
     deleted_files = pre_file - current_file
     if deleted_files :
         file_list=", ".join(deleted_files)
         print(f"[detect] 탐지날짜:{day} {hour}, 탐지된 삭제 파일명:{file_list}")

     pre_file = current_file 
     time.sleep(1) # 시스템 리소스 보호로 1초마다 탐지하게 함

