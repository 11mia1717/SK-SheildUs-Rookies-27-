import ftplib
#사용자 함수 정의
def upload_file(ftp, filename):
    with open(filename, 'rb') as f:
        ftp.storbinary(f'StOR {filename}', f) #같은 파일이름으로 저장

def main():
    hostname = "192.168.18.128"
    ftp = ftplib.FTP(hostname)
    ftp.login('msfadmin', 'msfadmin')

    #정의 함수 만들기는 가장 위에서 !
    upload_file(ftp, 'malwares.txt') #파일을 함수에 보내겠다.
    ftp.retrlines('LIST')

    ftp.quit()

#파이썬이 시작하는 시점임.
if __name__ == "__main__":
    main()

"""gpt
"이 파일을 직접 실행했을 때만 main()을 실행하고, 
import 될 때는 실행하지 마라" 라는 파이썬의 표준 관용구
"""