#https://www.malware-traffic-analysis.net/2023/index.html 를 크롤링 해서
#1. 제목 주소를 가져오시오.
#2. 링크 정보를 전체 URL 형식으로 출력하세요. (https://www.malware-traffic-analysis.net 로 시작)
#3. 결과 값을 txt 파일로 저장하세요.!!


import requests
from bs4 import BeautifulSoup

url = "https://www.malware-traffic-analysis.net/2023/index.html"

header_info = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

r = requests.get(url, headers=header_info)
soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.select("#main_content > div.content > ul > li > a.main_menu")
title_urls = soup.find_all("a")

with open('malware_url.txt', 'w', encoding='utf-8') as file:
    for title, title_url in zip(titles, title_urls):
        file.write(f"제목 : {title.text}\n")
        file.write(f"주소 : https://www.malware-traffic-analysis.net/2023/{title.get('href')}\n")
        print(f"제목 : {title.text}")
        print(f"주소 : https://www.malware-traffic-analysis.net/2023/{title.get('href')}")
