from pymongo import MongoClient
import shodan

#shodan에서 데이터 정보 가져오기
# Shodan API 키를 설정
SHODAN_API_KEY = 'Bh2LpaIgqG4x4fxhsOZEbWNwkChvQFR7'
api = shodan.Shodan(SHODAN_API_KEY)

# MongoDB 서버에 연결 (로컬호스트, 기본 포트 27017)
client = MongoClient('mongodb://localhost:27017')
#데이터 베이스 선택(없으면 자동생성)
db = client ['shodan_db']
#컬렉션 선택(없으면 자동생성)
collection = db['webcam_results']


# 웹캠을 검색합니다.
query = 'webcam'
results = api.search(query)

print(f"총 결과 : {results['total']}")


for match in results['matches'][:2]:
    data = {
        "ip" : match['ip_str'],
        "port": match['port'],
        "org": match.get('org', 'N/A'),
        "location": match['location']['country_name'],
        "hostnames": ', '.join(match['hostnames']) if match['hostnames'] else 'N/A'
    }
    collection.insert_one(data)
    