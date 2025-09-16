from flask import Flask, render_template, request, send_file
import os
from datetime import datetime
import zipfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def list():
    UPLOAD_PATH = 'uploads'
    files = []  #리스트 형태로

    #파일 정보를 리스트 형태로 가져옴

    for file in os.listdir(UPLOAD_PATH):
         #파일의 속성정보(size, ctime)
        file_path = os.path.join(UPLOAD_PATH, file)
        file_size = os.path.getsize(file_path)
        #file_ctime = os.path.getctime(file_path)
        file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d, %H:%M:%S')
        print(f"경로: {file_path}, 크기: {file_size}, ctime: {file_ctime}")
        """
        경로uploads\01_monitor.py, 크기: 1830, ctime: 2025-09-16 09:28:05.376312
        경로uploads\02_crawl_01.py, 크기: 1754, ctime: 2025-09-16 09:28:05.368660
        경로uploads\02_file_02.py, 크기: 1503, ctime: 2025-09-16 09:28:05.372049
        """

        # files.append(file, file_size) 한번에 넣으려고 하려면? -> 묶어야한다 
        #1. 키밸류 형식으로 갈 수도 있겠지만..(가능)
        #2. 리스트의 리스트->튜플? [(file, file_size, file_ctime), (file, file_size, file_ctime)...]
        #2번의 이유, 가볍고 간단
        files.append((file, file_size, file_ctime, file_path))
        #print(files)
        """
        [('01_monitor.py', 1830, '2025-09-16, 09:28:05', 'uploads\\01_monitor.py'), 
         ('02_crawl_01.py', 1754, '2025-09-16, 09:28:05', 'uploads\\02_crawl_01.py')....]

        """
        
    return render_template('list.html', files=files)


@app.route('/compress', methods=['GET', 'POST'])
def compress():
    UPLOAD_PATH = 'uploads'
    files = request.form.getlist("files")
    zip_path = os.path.join(UPLOAD_PATH, "compress.zip")

    with zipfile.ZipFile(zip_path, "w") as zip_file:
         for file in files:
              file_path = os.path.join(UPLOAD_PATH, file)
              zip_file.write(file_path, file)

    return send_file(zip_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)