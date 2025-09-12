#pip install feedparser #RSS/Atom 
#pip install pandas 로 라이브러리 설치
#pip install openpyxl 파이썬에서 엑셀파일을 제어하는 것

import feedparser
# 피드 파싱 라이브러리
#- 뉴스, 블로그 업데이트 등 XML 기반 피드를 쉽게 가져와서 파이썬 객체 형태로 변환

import pandas as pd #pd로 이름한다
#pandas : 데이터분석, 통계에 쓰이는 라이브러리

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)
#print(feed)

#링크 정의
titles = []
links = []
descriptions = []
authors = []
pubDates = [] 

for entry in feed.entries: #기사 한개 한개
    #print(entry) #딕셔너리 방식 {a:a, b,b} key&Value 쌍으로
    #print(entry.title) #타이틀 정보만 가져오기
    titles.append(entry.title) #titles 리스트에 저장
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

#print(pubDates)    #['2025-09-12 09:40:58', '2025-09-12 09:22:37']


data = {"제목": titles, "링크": links, "요약": descriptions, "작성자": authors, "날짜":pubDates}

#표? 처럼 만들기 위해 pandas 사용
df = pd.DataFrame(data)
#print(df)
"""
                                                   제목  ...                   날짜
0   KT 소액결제 해킹, 펨토셀 수법으로 드러나…KT 개인정보 유출 인정…용의자 검거후...  ...  2025-09-12 09:40:58
1              마이디어, 상하이에 '이노베이션 파크' 오픈…R&D·혁신 허브로 도약  ...  2025-09-12 09:22:37
"""

df.to_excel('데일리시큐.xlsx', index=False) #엑셀파일로 저장
print("파일이 생성")