from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <div data-role="page" data-last-modified="2022-01-01" data-foo="value">This is a div with data attributes.</div>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2" data-info="more info">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3" data-info="even more info">Tillie abcd</a>
    ; and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify()) #예쁘게 출력
#print(soup) #근데 똑같음

#태그 접근
print(soup.title) #soup: html 데이터중에서 title이 있으면 가져와
print(soup.title.string) #string 값만 가져오게 할때

#보안적인 관점 - Tomcat 5.5 취약점이 발생!!!
#전사 서비스 대상으로 우리 회사도 Tomcat 5.5 사용할까 확인
#자동화를 이용해,, 타이틀에 5.5가 있는지 확인! 


print(soup.p) #p태그를 찾아라, 일단 한개만 가져옴
print(soup.p['class']) #p태그 의 class의 값

print(soup.find_all('a')) #전체를 찾는다. 리스트방식

#출력을 위한 for구문
for link in soup.find_all('a'):
    print(link) #리스트안에 있는 <a>태그를 하나씩 변수에 담아 출력

    print(link.string) #태그안에 글자, 문자열 부분만 가져온다.
    print(link.get('href')) #attribute 속성값을 가져온다.