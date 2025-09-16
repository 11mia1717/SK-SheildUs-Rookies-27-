from pymongo import MongoClient

# MongoDB 서버에 연결 (로컬호스트, 기본 포트 27017)
client = MongoClient('mongodb://localhost:27017')
#데이터 베이스 선택(없으면 자동생성)
db = client ['school_db']
#컬렉션 선택(없으면 자동생성)
collection = db['students']

# 전체 데이터 찾기 find()
for student in collection.find():
    print(student)

print("===============================")
print(collection.find_one({"name":"장민아"}))

#조건에 맞는 문서 조회 (나이가 20이상인 학생)
print("\n나이가 20 이상인 학생 :")
#조건문 $great크거나 equal같다
for student in collection.find({"age":{"$gte":20}}):
    print(student)

