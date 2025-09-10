#import deep_translator
#deep_translator.GoogleTranslator.translate() #구글 번역과 관련된 함수


#from 라이브러리에서 가져올 것을 정의를 해둠
#GoogleTranslator.translate() 
#더 간단한 표현하게 표현이 가능
from deep_translator import GoogleTranslator

#구글 번역을 통해 영어로 번역
# 'es' : 'Spanish' 'fr' : 'French' ... 'ja' : 'Japanese'....
input_text = input("번역할 한글을 입력하세요. \n입력 : ")
translated = GoogleTranslator(source='ko', target='en').translate(input_text)

#fstring을 이용하여 출력 print(f"{}") 형태 기억해두기
print(f"\n입력한 한글 : {input_text}")
print(f"번역된 영어 : {translated}")