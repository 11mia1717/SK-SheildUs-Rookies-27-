from flask import Flask, redirect, render_template
from pymongo import MongoClient
from bson import ObjectId

#Mongo DB 연결정보
client = MongoClient("mongodb://localhost:27017")
db = client['mydatabase_faker']
collection = db['people']


app = Flask(__name__)

@app.route('/', methods=['GET'])
def db():
   
    # 전체 데이터를 가져오기
    people = collection.find()
    print(people)
    """
    [{'_id': ObjectId('68c8fd9f679acdab0209f534'), 'name': '김지민', 'address': '경상북도 고양시 일산서구 봉은사029거리 312 (영식나백동)', 'email': 'myeongja87@example.org', 'phone': '044-360-2990'}, 
    {'_id': ObjectId('68c8fd9f679acdab0209f535'), 'name': '권영환', 'address': '경상북도 의왕시 강남대2길 401-35', 'email': 'songsugja@example.org', 'phone': '062-374-8017'}, ....]
    """
    return render_template('db.html', people=people)

@app.route('/delete_user/<user_id>') #파라미터를 통해 변수를 받을때 
def delete_user(user_id): #받은 변수를 표기해준다.
    # 선택한 유저의 데이터를 지우기
    # 여러 문서 삭제 
    collection.delete_one({'_id':ObjectId(user_id)})
    ##_id = MongoDB의 기본 Primary Key ObjectId = MongoDB가 생성하는 특별한 타입 → Flask에서 URL로 전달받은 문자열을 ObjectId(user_id) 로 변환해줘야 MongoDB가 인식할 수 있습니다.

    #return render_template으로 보내도 됨
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 
