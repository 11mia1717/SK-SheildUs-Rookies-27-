from docx import Document
from docx2pdf import convert

#플라스크에서 구현하기 --퀴즈
#1. 사용자에게 이름, 교육명, 날짜를 입력받고
#2. 발급하기 버튼을 클릭하면
#3. 수료증 생성 및 변환 → 다운로드 페이지에서 발급 가능

name = input("이름을 입력하세요 : ")
course = input("과정을 입력하세요 : ")
date = input("수료 날짜를 입력하세요 : ")

doc = Document('template.docx')

#각각 개체들을 불러옴
for paragraph in doc.paragraphs:
    #print(paragraph.text)
    """
    출력값 이렇게(객체의 메모리 주소) 되는데 .text를 붙여서 눈에 보이게
    <docx.text.paragraph.Paragraph object at 0x0000021B4A225BE0>
    <docx.text.paragraph.Paragraph object at 0x0000021B4A127610>
    <docx.text.paragraph.Paragraph object at 0x0000021B4A127750>
    """

    if 'NAME' in paragraph.text: #불러온 값에 NAME 값이 있다면
        paragraph.text = paragraph.text.replace('NAME', name)

    elif 'COURSE' in paragraph.text:
        paragraph.text = paragraph.text.replace('COURSE', course)
    
    elif 'DATE' in paragraph.text:
        paragraph.text = paragraph.text.replace('DATE', date)

#문서를 저장
doc_filename = f"{name}_{course}_수료증.docx"
pdf_filename = f"{name}_{course}_수료증.pdf"

doc.save(doc_filename)
convert(doc_filename, pdf_filename)