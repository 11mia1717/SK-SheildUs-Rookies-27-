import ftplib

hostname = "192.168.18.128"
ftp = ftplib.FTP(hostname)

ftp.login('msfadmin', 'msfadmin')
print(ftp.pwd())
#명령어 수행시 사용하는 함수
ftp.retrlines('LIST') #ftp에게 LIST명령어를 준다
#cf)ftp.retrbinary는 파일을 검색하여 다운로드
print("==============")
ftp.mkd("new_folder")
ftp.retrlines('LIST')
print("==============")
ftp.cwd("vulnerable")
ftp.retrlines('LIST')

print("==============")
ftp.rmd("vulnerable")
ftp.retrlines('LIST')
ftp.quit()