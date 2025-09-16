#PBL2_RSS서비스를 이용하여 매일 정보를 수집해서 이슈를 확인하려고 한다.
#하지만, 출근 길에 운전을 하느라 화면을 볼 수 없어
#음성으로 변환해서 저장해서 들을 예정이다.
import feedparser
from gtts import gTTS
from datetime import datetime


def format_date(date_string):
    #날짜를 읽기 좋게 포맷하는 함수
    try:
        # RSS의 날짜 포맷을 파싱해서 읽기 좋게 변환
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        year = str(parsed_date.year) + '년'
        month = str(parsed_date.month) + '월'
        day = str(parsed_date.day) + '일'
        return f"{year} {month} {day}"
    
    except: #포맷이 다를 경우 원본을 유지
        return date_string


def get_rss_data(url):    
    #RSS 피드에서 데이터를 가져오는 함수

    feed = feedparser.parse(url)
    #print(feed)    #가져온 데이터 값 확인
    print(f"[log]데일리시큐 RSS 이슈 데이터 추출 성공")

    # 각 기사 정보 entry를 딕셔너리로 만들어 리스트에 저장
    data = []
    for entry in feed.entries:
        text = {
            "제목": entry.title, 
            "요약": entry.summary, 
            "작성자": entry.author, 
            "날짜":format_date(entry.published)
            }
        data.append(text)

    print(f"[log]RSS 이슈 데이터를 딕셔너리 리스트로 저장 성공 - 총 {len(data)}개")

    return data


def create_tts_text(data):
    # tts 음성으로 읽을 수 있는 텍스트를 생성하는 함수

    tts_texts = []
    # 오늘 날짜를 읽을 수 있는 형식으로 변환
    today = datetime.now().strftime('%Y년 %m월 %d일')

    #텍스트 시작 부분
    tts_texts.append(f"""
        {today}의 데일리시큐 보안 이슈를 읽어드리겠습니다.
        총 {len(data)}개의 이슈가 있습니다.
        """)

    #텍스트 데이터 부분
    for i, value in enumerate(data):
        text = f"""
        {i+1}번째입니다.
        제목 {value['제목']}
        내용 요약 {value['요약']} 이하 생략합니다.
        작성자는 {value['작성자']} 입니다.
        게시일은 {value['날짜']} 입니다.
        """
        tts_texts.append(text.strip())

    #텍스트 마무리 부분
    tts_texts.append(f"이상으로 {today}의 데일리시큐 보안 이슈를 마치겠습니다.")

    # 리스트tts_texts를 문자열로 합쳐주기
    all_tts_text ="\n".join(tts_texts)
    
    return all_tts_text, today
    

def save_to_mp3(text, today):
    #읽기 적합한 를 gTTS를 이용해서 mp3파일로 생성 및 저장
    language = 'ko' # 한국어
    tts = gTTS(text=text, lang=language)

    filename = f"DailySecu_Issue_{today}.mp3"
    tts.save(filename)
    print("[log]음성 파일 생성 완료")

    return filename


def main():
    #메인함수

    #데일리 시큐 RSS 이슈 url 정보
    url = "https://www.dailysecu.com/rss/S1N2.xml"
    #RSS 피드에서 데이터를 가져오는 함수
    data = get_rss_data(url)

    #TTS 읽기용 텍스트 
    all_tts_text, today = create_tts_text(data)
    print(f"[log]gTTS 스크립트 정보: {all_tts_text}")

    #음성 파일로 저장하기(mp3)
    filename = save_to_mp3(all_tts_text, today)
    
    

if __name__ == "__main__":
    #메인함수를 호출    
    main()            