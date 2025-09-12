#read() 파일의 내용을 통째로 읽어온다 
# (장단점 - 속도 빠름, 개인정보가 몇개고 몇번째 줄인지 파악하기는 어려움)
#readline() 한줄 씩 읽는다.
#readlines() 

# 'with' 문을 사용하여 파일을 열고 자동으로 닫기

#read()
# 'r' read가 추가됨 :파일의 내용을 통째로 읽어온다
with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.read()
    print(content)

print("="*50)
# readline() :  한줄 씩 읽는다.
with open('example.txt', 'r', encoding='utf-8') as helloFile:
    print(helloFile.readline())  # 첫 번째 줄 읽기
    print(helloFile.readline())  # 두 번째 줄 읽기

print("="*50)
#readlines() 리스트 형태로
with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.readlines()
    print(content)