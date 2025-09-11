#ZDNET의 필요한 정보 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://zdnet.co.kr/"

# User-Agent를 정의
header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'} 
# Why? 바로 요청하게 되면 처음은 괜찮지만, 
# user-agent 정보가 없으면 비정상이라고 생각하기 때문에 적어주기

#웹페이지 가져오기
r = requests.get(url, headers=header_info) #url주소로 요청을 보냄 +헤더정보를 담아서
#가져온 html을 분석할 수 있는 형태로 바꾸기
soup = BeautifulSoup(r.text, 'html.parser') #r.text : 응답받은 HTML 원본 텍스트


#원하는 부분만 가져오려면 soup.selector()
#links = soup.select("body > div.contentWrapper > div:nth-child(1) > div.left_cont > div.news1_box > div.news_list > div:nth-child(1) > div.assetText > a > h4")
links = soup.select("div.news1_box > div.news_list > div:nth-child(1) > div.assetText > a > h4")
#F12, selected element, 원하는 것선택, 우클릭, copy > copy selector
# nth이하 생략해야(그룹으로 되어있는것임) 전체를 다 가져올것
#print(soup)

for link in links:
    print(link.string)


