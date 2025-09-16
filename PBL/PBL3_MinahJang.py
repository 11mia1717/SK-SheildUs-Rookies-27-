#디렉토리 파일 감지 시스템 구축
#보안 담당자는 중요한 서버에 업로드 되는 파일에 
#개인정보가 포함되어있는지 여부를 모니터링 하고 싶다.
#외부에 중요 정보가 노출이 되기 전에 잠재적 보안 위협을 방지하고 싶어한다.

import os
import re
import time
from datetime import datetime 


#보안 탐지 함수(파일 내용에서 중요 정보를 탐지하는 함수) 
def check_security_file(file_path, file_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        count = 0 #탐지된 항목 카운트

        for index, line in enumerate(lines):
            #주석처리 텍스트 탐지(코드 앞줄 #, //로 시작)
            if ( 
                line.strip().startswith("#") 
                or line.strip().startswith("//")
                or line.strip().startswith("<!--")
            ):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, 주석처리 된 코드 탐지")
                count += 1

            #키워드 정의
            pw_words = ['암호', '비밀번호', 'password', 'passwd', 'pw', '키', 'key']
            #비밀번호 관련 키워드 탐지
            if any(word in line.lower() for word in pw_words):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, 비밀번호 관련 키워드 탐지")
                count += 1

            #주민번호 탐지
            if re.search(r'\b\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\s*-\s*[1-4]\d{6}\b',line):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, 주민번호 탐지")
                count += 1
            
            #전화번호 또는(|) 핸드폰 번호 탐지
            if re.search(r'\b0\d{1,2}\s*-\s*\d{3,4}\s*-\s*\d{4}\b|\b01[016789]\s*-\s*?\d{3,4}\s*-\s*?\d{4}\b',line):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, 전화번호/핸드폰 번호 탐지")
                count += 1
            
            #이메일 주소 탐지
            if re.search(r'[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9.-]+\.)[A-Za-z]{2,}',line):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, 이메일 주소 탐지")
                count += 1

            #IP주소 탐지
            if re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line):
                print(f"[detect] 신규 파일 {file_path}, {index+1}라인, IP주소 탐지")
                count += 1



        #신규 파일 내용 검사 완료 로그
        if count == 0: 
            print(f"[log] 신규 파일 {file_name} 보안 검사 완료 - 특이 사항 없음")
        else:
            print(f"[warn] 신규 파일 {file_name} 에서 총 {count}개의 잠재적 보안 위협 요소 탐지")


#메인함수
def main():
    #특정 디렉토리 경로 지정
    dir_path = "Security_Check"

    #디렉토리가 없으면 생성
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"[log] {dir_path} 디렉토리를 생성했습니다.")

    #초기 디렉터리 안의 파일을 확인(pre_file), 리스트간 비교를 위해 형변환
    pre_file = set(os.listdir(dir_path)) 

    print(f"[log] {dir_path} 탐지 경로 확인했습니다 ")
    print(f"[log] 보안 폴더 모니터링 시작...")

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
        
        #신규 탐지된 파일 확인
        if new_files :
            file_list=", ".join(new_files)
            print(f"[detect] 탐지 날짜:{day} {hour}, 탐지 된 신규 파일목록 : {file_list}")
            
            #디렉터리 내 신규 추가 파일들을 하나씩 중요정보 확인 후 탐지 결과 출력
            for new_file in new_files:
                #신규 파일 경로 정의
                file_path = os.path.join(dir_path, new_file)

                #파일 내용 보안 검사
                check_security_file(file_path, new_file)      

        #삭제된 파일 확인
        deleted_files = pre_file - current_file
        if deleted_files :
            file_list=", ".join(deleted_files)
            print(f"[log] 탐지 날짜:{day} {hour}, 삭제 파일목록: {file_list}")

        pre_file = current_file 
        time.sleep(2) # 시스템 리소스 보호로 2초마다 탐지하게 함


if __name__ == "__main__":
    #메인함수를 호출    
    main()            