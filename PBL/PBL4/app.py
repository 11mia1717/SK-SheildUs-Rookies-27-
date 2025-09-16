#PBL-4, FLASK FTP 서버 구축
#반복되는 업무 결과를 효율적으로 처리하기 위한 방안 지시가 내려왔다.
#FTP 서비스에 수시로 파일들이 저장되어 처리되고 있는데,
#이를 자동으로 목록화 해주는 작업을 자동화 할 계획이다.

from flask import Flask, render_template, request, redirect
import ftplib

app = Flask(__name__)


@app.route("/") 
def login(): 
    return render_template('login.html')

@app.route("/ftp_login", methods=['GET', 'POST']) 
def ftp_login():
    #로그인 정보를 변수로 받아온다 
    ip_addr = request.form['ip_addr']
    user_name = request.form['user_name']
    user_pw = request.form['user_pw']
    try: 
        #FTP 연결 및 로그인
        ftp = ftplib.FTP(ip_addr)
        ftp.login(user_name, user_pw)
        #print(ftp.pwd()) #현재 경로 출력하여 로그인 성공 여부 확인

        #print(ftp.retrlines('LIST')) #파일 리스트 출력확인
    
        # 파일 리스트를 저장할 리스트 생성
        file_list = []
            
        # 콜백 함수를 사용하여 파일 목록을 리스트에 추가
        ftp.retrlines('LIST', callback=lambda line:file_list.append(line))
        print(file_list)
        """
        ['-rw-r--r--    1 1000     1000            0 Sep 12 07:13 ftp_security.txt', 
        '-rw-r--r--    1 1000     1000            0 Sep 12 05:19 malwares.txt', 
        'drwxr-xr-x    2 1000     1000         4096 Sep 12 04:57 new_folder', 
        '-rw-r--r--    1 1000     1000        45839 Sep 12 06:26 result.zip', 
        'drwxr-xr-x    6 1000     1000         4096 Apr 28  2010 vulnerable']
        """
        #FTP 연결 종료
        ftp.quit()

        return render_template('index.html', file_list=file_list)

        
    except Exception as e:          
        #에러 처리
        msg=f"FTP 연결 오류: {str(e)}"
        return render_template('login.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)