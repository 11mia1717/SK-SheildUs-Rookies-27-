from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['school_db']
collection = db['students']

# 단일 문서 업데이트 (김철수의 학년을 A+로 변경)
result = collection.update_one(
    {"name": "김철수"},
    {"$set": {"grade": "A+"}}
)
print(f"수정된 문서 수: {result.modified_count}")

# 여러 문서 업데이트 (수학 과목을 수강하는 학생들의 학년을 B로 변경)
result = collection.update_many(
    {"subjects": "수학"},
    {"$set": {"grade": "B"}}
)
print(f"수정된 문서 수: {result.modified_count}")