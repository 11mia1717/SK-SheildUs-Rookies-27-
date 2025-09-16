#1. uploads 폴더를 모니터링한다.
#2. 새로운 파일이 생성이 되면, 슬랙에 "OOOO 파일이 생성되었습니다." 메시지와 함께, 파일을 보내세요.
#<추가사항>
#1. 파일 내에 주민번호 있다면?!! <주민번호 포함> 메시지와 함께...
#.....등등등...
# ->(추가) 주민번호 뒤를 마스킹 처리 변환 해서 보내거나... 건수만 확인...


import os
import time
from datetime import datetime 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


dir_path = "uploads"
pre_file = set(os.listdir(dir_path)) 
print(f"pre_file{pre_file}")


#print(os.getcwd())  # 현재 작업 경로 확인
#print(os.path.exists("list.txt"))

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "xoxb-9502554741763-9506588087618-cTrNl3twMC7MCtx61S9EUgq8" #Api페이지에서의 Oauth 토큰값
SLACK_CHANNEL = "C09EWG63HC2" #채널세부정보의 채널ID값
# 채널 접근 후 URL 뒤에서 확인 가능

def upload_file(channel, file_path, message):
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_API_TOKEN)
    
    try:
        # 파일을 Slack 채널에 업로드하고, 해당 파일에 메시지를 추가합니다.
        response = client.files_upload_v2(
            channel=channel, 
            file=file_path,
            initial_comment=message
        )
        # 업로드 성공 메시지 출력
        print("File uploaded successfully:", response["file"]["name"])
    except SlackApiError as e:
        # 에러 처리
        print("Error uploading file:", e.response["error"])



        
if __name__ == "__main__":
    while True:
        time.sleep(1)
        print(".....모니터링 중........")  
        current_file = set(os.listdir(dir_path))
        result_diff = current_file - pre_file 

        #print(f"파일 생성 : {result_diff}")
        for file in result_diff :
            file_path = os.path.join(dir_path, file)
        # 파일 업로드 및 메시지 전송 함수 호출
        upload_file(SLACK_CHANNEL, result_diff, f"{result_diff}파일 생성이 탐지되었습니다.")

        pre_file = current_file
        


