#네이버 지식인에 keyword 을 검색했을 때
#제목과 날짜 가져오기

import requests
from bs4 import BeautifulSoup

keyword = input("키워드 입력 : ")
url = f"https://kin.naver.com/search/list.naver?query={keyword}"

header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'} 


r = requests.get(url, headers=header_info) 
soup = BeautifulSoup(r.text, 'html.parser') 

titles = soup.select("#s_content > div.section > ul > li > dl > dt > a")
dates = soup.select("#s_content > div.section > ul > li > dl > dd.txt_inline")

#for title in titles:
#    print(f"질문 : {title.string}")

#title.text는 결과값을 잘 보여주는데 title.string으로 했는데 왜 none이라고 뜰까요?
#text는 사람이 볼 수있는 형태 
#string의 경우 자식태그가 있으면 none을 반환한다.

for date, title in zip(dates, titles): #리스트 형식에서 뽑아쓸때
    print(f"날짜: {date.text}")
    print(f"질문: {title.text}")