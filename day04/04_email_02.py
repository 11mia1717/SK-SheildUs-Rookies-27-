import smtplib
from email.mime.multipart import MIMEMultipart #웹서비스에서 많이 사용하는 모듈, Flask
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
from dotenv import load_dotenv
import os

load_dotenv()
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "mingna14@naver.com"

smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login(send_email,send_pwd)
  
text = f"탐지라인:"

#본문 메세지 작성
msg = MIMEMultipart()
msg['Subject'] = f"모니터 탐지:"  
msg['From'] = send_email          
msg['To'] = recv_email

text ="<b>탐지되었습니다.</b>"

contentPart = MIMEText(text) 
msg.attach(contentPart)  #attach로 내용을 붙여 보낸다.

etc_file_path = r'uploads/file.txt' #보낼 파일 #r은 이스케이프 문자를 무시하고 "있는 그대로" 문자열을 처리
with open(etc_file_path, 'rb') as f : 
    etc_part = MIMEApplication( f.read() )
    etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
    msg.attach(etc_part) #attach로 첨부파일 붙이기

smtp.sendmail(send_email,recv_email,msg.as_string() )
smtp.quit()