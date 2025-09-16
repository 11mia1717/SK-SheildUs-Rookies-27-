#엑셀로 만드는 실습해보기

#1. 한글로 되어 있는 test.txt 파일  
#   -> (추가로 해보세요) RSS 서비스로 엑셀 수집 -> 한글 -> 영문으로 번역한 결과
#2. 영문으로 번역을 한다.
#3. 결과 값을 메일로 보낸다. 메일 제목은 {OOOO} 파일 번역 결
#4. 번역 결과 txt 파일에는 "변역된 시간", "원문", "번역문"이 포함
import smtplib
from email.mime.multipart import MIMEMultipart #웹서비스에서 많이 사용하는 모듈, Flask
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time 
from dotenv import load_dotenv
import os
from datetime import datetime 
import feedparser
from openpyxl import Workbook
from deep_translator import GoogleTranslator


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


def rss_data_and_translate():
    ##RSS 서비스 대상으로 정보 수집 및 엑셀 파일 저장
    #저장 디렉토리명
    RESULT_DIR = "rss_result"

    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

    #현재 시간 표시
    now = datetime.now() 
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")

    #번역기 초기화(한글 번역)
    translator = GoogleTranslator(source='ko', target='en')

    #파일을 열어 URL 정보를 한줄씩 가져오기
    with open('list.txt', 'r', encoding='UTF-8') as file:
        rss_urls = file.readlines()
        print(f"RSS URL:{rss_urls}")

    #번역문 리스트 정리
    translated_files = []

    #각 데이터 값를 리스트에 정의
    for index, url in enumerate(rss_urls):
        print(f"{index+1}번째 RSS처리 중...")

        feed = feedparser.parse(url)
        titles = []
        links = []
        descriptions = []
        authors = []
        pubDates = []

        for entry in feed.entries:
            titles.append(entry.title)
            links.append(entry.link)
            descriptions.append(entry.description)
            authors.append(entry.author)
            pubDates.append(entry.published)

        # 워크북과 워크시트를 생성합니다.
        wb = Workbook()
        
        #원문시트
        ws_org = wb.active
        ws_org.title = f"{index+1}번째 원문 Data"

        #번역문 시트
        ws_translated = wb.create_sheet(title=f"{index+1}번째 번역 데이터")

        # 원문 시트 헤더작성
        headers = ['Title', 'Link', 'Description', 'Author', 'Published']
        ws_org.append(headers)
        
        # 번역문 시트 헤더작성
        translated_headers = ['번역시간', 'Translated Title', 'Link','Translated Description', 'Author', 'Published']
        ws_translated.append(translated_headers)

        # 원문 데이터 작성
        for i in range(len(titles)):
            ws_org.append([titles[i], links[i], descriptions[i], authors[i], pubDates[i]])

        print(f"번역 시작 - {len(titles)}개 항목")


        # 번역 데이터 작성
        for i in range(len(titles)):
            print(f"번역 진행: {i+1}/{len(titles)}")
            
            # 제목과 설명만 번역 (링크, 저자, 날짜는 그대로 유지)
            translated_title = translate_text(titles[i], translator)
            translated_desc = translate_text(descriptions[i], translator)
            
            ws_translated.append([
                f"{day} {hour}",  # 번역시간
                translated_title,  # 번역된 제목
                links[i],         # 링크 (번역 안함)
                translated_desc,  # 번역된 설명
                authors[i],       # 저자 (번역 안함)
                pubDates[i]       # 발행일 (번역 안함)
            ])

        # 엑셀 파일로 저장합니다.
        file_path = os.path.join(RESULT_DIR, f'{index+1}_result.xlsx')
        wb.save(file_path)

        translated_files.append(file_path)
        print(f"저장 완료: {file_path}")

        return translated_files

def translate_text(text, translator):
    """텍스트를 번역하는 함수 (에러 처리 포함)"""
    try:
        if text and str(text).strip():
            # API 요청 제한을 위한 짧은 대기
            time.sleep(0.1)
            return translator.translate(str(text))
        return text
    except Exception as e:
        print(f"번역 오류: {e}")
        return text
    
def main():
    
    print("RSS 데이터 수집 및 번역 시작...")

    # RSS 데이터 읽어와서 엑셀 파일로 저장하고 번역
    translated_files = rss_data_and_translate()

    print(f"번역이 완료되었습니다. {len(translated_files)}개 파일이 생성되었습니다.")
    
    # 각 번역된 파일을 메일로 전송
    for file_path in translated_files:
        print(f"메일 전송 중: {file_path}")
        mail_sender(file_path)
        print(f"메일 전송 완료: {file_path}") 

if __name__ == "__main__":
    main()