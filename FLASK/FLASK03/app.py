from docx import Document
from docx2pdf import convert
from flask import Flask, render_template, request, send_file
import os

#플라스크에서 구현하기 --퀴즈
#1. 사용자에게 이름, 교육명, 날짜를 입력받고
#2. 발급하기 버튼을 클릭하면
#3. 수료증 생성 및 변환 → 다운로드 페이지에서 발급 가능

#1. 파이썬 플라스크를 이용하여 사용자 페이지 / 결과 페이지(다운로드) 제작
#2. 사용자에게 이름, 과정, 날짜를 입력받는다.
#3. 자동으로 docx와 pdf 파일을 생성한다.
#4. PDF 수료증을 다운로드 받게 안내한다.

app = Flask(__name__)

@app.route("/") 
def index(): 
    return render_template('index.html')
    
@app.route("/doc", methods=['GET', 'POST']) 
def doc(): 
    name = request.form['name']
    course = request.form['course']
    date = request.form['date']

    #참고할 템플릿 파일 정의
    doc = Document('template.docx')

    #각각 개체들을 불러옴
    for paragraph in doc.paragraphs:
        #print(paragraph.text)
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
    return render_template('result.html', pdf_filename=pdf_filename)
    ### pdf_filename 변수를 아래에서 읽어올 수 있게 선언해서 html에 넘겨주기!


@app.route("/download_pdf") 
def download_pdf(): 
    pdf_filename = request.args.get('pdf_filename')
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(BASE_DIR, pdf_filename)  # 절대경로 만들기
    return send_file(full_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 
