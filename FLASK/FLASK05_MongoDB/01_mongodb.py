from pymongo import MongoClient

# MongoDB 서버에 연결 (로컬호스트, 기본 포트 27017)
client = MongoClient('mongodb://localhost:27017')

#용어의 차이 
#mysql, mssql, oracle - 데이터베이스 > 테이블 > 컬럼 > 데이터 로 비슷하나,
#mongodb - 데이터베이스 - 컬렉션(collection) - 데이터(object)로 용어가 다름
#elasticsearch - 인덱스 - 문서(document) - 데이터...

#데이터 베이스 선택(없으면 자동생성)
db = client ['school_db']

#컬렉션 선택(없으면 자동생성)
collection = db['students']

#print("MongoDB에 성공적으로 연결되었습니다!")
"""
#Key, Value 형식으로 들어감
student = { #하나의 데이터 정의
    "name":"장민아",
    "age":20,           #Value값은 문자, 숫자 등 형태상관없음
    "grade":"A",
    "subjects" : ["수학", "영어"]
}


#컬렉션에 데이터 하나 넣기 insert_one(하나의 데이터)
# cf) insert_many(여러개의 데이터)
result = collection.insert_one(student)

print(f"추가된 문서 ID: {result.inserted_id}")
#추가된 문서 ID: 68c8f28fc2ff5fcf56d8153e 유일한 값으로 구분이 됨(hash 값)
"""
#여러 데이터 삽입
# 여러 문서 삽입
students = [
    {"name": "이영희", "age": 19, "grade": "B", "subjects": ["과학", "국어"]},
    {"name": "박민수", "age": 21, "grade": "A", "subjects": ["수학", "과학"]}
]
#컬렉션에 데이터 여러개 넣기 insert_many(여러개의 데이터)
result = collection.insert_many(students)
print(f"삽입된 문서 ID들: {result.inserted_ids}")