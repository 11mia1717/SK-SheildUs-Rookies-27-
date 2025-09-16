from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "xoxb-9502554741763-9506588087618-cTrNl3twMC7MCtx61S9EUgq8" #Api페이지에서의 Oauth 토큰값
SLACK_CHANNEL = "C09EWG63HC2" #채널세부정보의 채널ID값

def send_message(channel, text):
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_API_TOKEN)
    
    try:
        # 채널에 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        # 응답 출력
        print("Message sent successfully:", response["message"]["text"])
    except SlackApiError as e:
        # 에러 처리
        print("Error sending message:", e.response["error"])

# 메시지 전송 함수 호출
send_message(SLACK_CHANNEL, "Hello, this is a TEST message from Slack API!")
send_message(SLACK_CHANNEL, "안녕 난 테스트메세지야")