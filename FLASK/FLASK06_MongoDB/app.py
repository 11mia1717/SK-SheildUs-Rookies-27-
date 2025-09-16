#1. Shodan 검색 결과 3개~5개를 mongodb 데이터베이스에 저장
#2. 플라스크로 데이터 정보 가져와서 html 출력

from flask import Flask, redirect, render_template
from pymongo import MongoClient
from bson import ObjectId

#Mongo DB 연결정보
client = MongoClient("mongodb://localhost:27017")
db = client['shoudan_db']
collection = db['webcam_results']

app = Flask(__name__)

@app.route('/')
def index():
    results = collection.find()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True) 