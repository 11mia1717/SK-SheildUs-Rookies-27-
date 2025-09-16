#1. 한글로 되어 있는 test.txt 파일  
#   -> (추가로 해보세요) RSS 서비스로 엑셀 수집 -> 한글 -> 영문으로 번역한 결과
#2. 영문으로 번역을 한다.
#3. 결과 값을 메일로 보낸다. 메일 제목은 {OOOO} 파일 번역 결
#4. 번역 결과 txt 파일에는 "변역된 시간", "원문", "번역문"이 포함
import smtplib
from email.mime.multipart import MIMEMultipart #웹서비스에서 많이 사용하는 모듈, Flask
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
from dotenv import load_dotenv
import os
import time
from datetime import datetime 

def mail_sender(report_file):
    load_dotenv()
    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")
    recv_email = "mingna14@naver.com"

    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(send_email,send_pwd)
    
    text = f"{report_file} 파일 번역 결과"

    #본문 메세지 작성
    msg = MIMEMultipart()
    msg['Subject'] = f"{report_file} 파일 번역 결과"  
    msg['From'] = send_email          
    msg['To'] = recv_email

    contentPart = MIMEText(text, 'html', 'utf-8') 
    msg.attach(contentPart)  

    etc_file_path = report_file
    with open(report_file, 'rb') as f : 
        etc_part = MIMEApplication( f.read() )
        etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
        msg.attach(etc_part) #attach로 첨부파일 붙이기

    smtp.sendmail(send_email,recv_email,msg.as_string() )
    smtp.quit()

#현재 시간 표시
now = datetime.now() #현재시간
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

file_name="test10.txt"

##파읽을 읽어 번역
from deep_translator import GoogleTranslator

#본문 읽기 리스트 형태로
with open(file_name, 'r', encoding='utf-8') as File:
    org_content = File.read()

#구글 번역을 통해 영어로 번역
transl_content = GoogleTranslator(source='ko', target='en').translate(org_content)
print(transl_content)

#파일에 리스트로 덮어쓰기
report_file = f'{file_name}_번역결과.txt'
with open(report_file, 'w', encoding='utf-8') as file:
    file.write(f"번역시간: {hour}\n")
    file.write(f"{file_name}파일의 내용\n")
    file.write(f"원문:\n{org_content}\n")
    file.write(f"번역문:\n{transl_content}\n")
    
print(f"번역이 완료되었습니다. 결과는 {report_file}에 저장되었습니다.")
mail_sender(report_file)   
