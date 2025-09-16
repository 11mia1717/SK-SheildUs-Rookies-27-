import requests

slack_url = "https://hooks.slack.com/services/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" #여러분의 Slack API 주소

def sendSlackWebHook(strText):
    headers = { #헤더정보
        "Content-type": "application/json"
    }
    
    data = { #데이터 정의
        "text": strText
    }

    #post(보낸다)
    res = requests.post(slack_url, headers=headers, json=data)
    
    if res.status_code == 200:
        return "OK"
    else:
        return "Error"

print(sendSlackWebHook("파이썬 자동화 슬랙 메시지 테스트"))