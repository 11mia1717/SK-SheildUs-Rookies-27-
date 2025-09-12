#정의함수를 활용

import feedparser
from openpyxl import Workbook
import os
import zipfile
import ftplib

##RSS 서비스 대상으로 정보 수집 및 엑셀 파일 저장
RESULT_DIR = "rss_result"

def rss_data():
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

    with open('list.txt', 'r', encoding='UTF-8') as file:
        rss_urls = file.readlines()
        print(rss_urls)

    for index, url in enumerate(rss_urls):
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
        ws = wb.active
        ws.title = f"{index+1}번째 Data"

        # 첫 번째 행에 헤더를 작성합니다.
        headers = ['Title', 'Link', 'Description', 'Author', 'Published']
        ws.append(headers)

        # 데이터를 행 단위로 작성합니다.
        for i in range(len(titles)):
            ws.append([titles[i], links[i], descriptions[i], authors[i], pubDates[i]])

        # 엑셀 파일로 저장합니다.
        file_path = os.path.join(RESULT_DIR, f'{index+1}_result.xlsx')
        wb.save(file_path)


def create_zip():
    ##결과 값을 result.zip 파일로 저장
    zip_file = zipfile.ZipFile("result.zip", "w")

    for root, dirs, files in os.walk(RESULT_DIR):
        for file in files:
            zip_file.write(os.path.join(root, file))

    zip_file.close()

def upload_ftp():
    ##FTP 서버에 결과 값을 보낸다.
    hostname = "192.168.81.128"
    ftp = ftplib.FTP(hostname)
    ftp.login('msfadmin','msfadmin')
    ftp.retrlines('LIST')

    with open("result.zip", "rb") as f:
        ftp.storbinary(f"STOR result.zip",f)

    print(f"현재작업디렉터리：{ftp.pwd()}")
    ftp.retrlines('LIST')
    ftp.quit()

def main():
    rss_data()
    create_zip()
    upload_ftp()

if __name__ == "__main__":
    main()