import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
#선언하는 부분
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "mingna14@naver.com" 

smtp_name = "smtp.naver.com"
smtp_port = 587              

text = "이메일 보내기 테스트입니다"

msg = MIMEText(text, "plain", 'utf-8') 
msg['Subject'] = "메일 제목"  
msg['From'] = send_email          
msg['To'] = recv_email            

#메일을 보내는 부분
email_string = msg.as_string() #메세지값을 스트링값으로
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls() #암호화 통신
s.login(send_email, send_pwd) #로그인
s.sendmail(send_email, recv_email, email_string) #메일 보내기
s.quit()