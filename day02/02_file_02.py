
import os

#디렉터리 리스트 뽑기 os.listdir()
files = os.listdir('.') # 현재 디렉토리 .
print(files)

for file in files: #하나씩 출력하는 for 구문
    print(file)
    
#ex. ['.git', '03_print.py', 'file.txt'] 
#['.git', '03_print.py', 'file.txt', uploads] 리스트 형태로 출력
#단, uploads가 폴더인기 파일인지 확인할 수 없음 (isdir로 확인해야) 
# 하위 디렉터리의 파일은 확인할 수 없음.(for문으로 물어볼 수 있음)
"""
for file in files: #하나씩 출력하는 for 구문
    if os.path.isdir(file): #디렉터리라면
        files_dir = os.path.isdir(file)
        for file in files_dir:
            print(f"{file}는 디렉터리") #출력
    print(file)
    #아 근데 안된다 ㅡㅡ
"""


#디렉터리 트리탐색 os.walk()
files = os.walk('.')
print(files) 
#<generator object walk at 0x0000024C676D0BC0>
#object walk ? 리스트 형태로 세개로 묶여잇는 것일 것이다.

for dirpath, dirnames, filenames, in files:
    print(f"Found directory: {dirpath}")
    print(f"Subdir: {dirnames}")
    print(f"File: {filenames}")
    print("-"*50)

"""
Found directory: .
Subdir: ['.git', 'uploads'] #하위 디렉터리도 찾는다
File: ['01_dic.py', '03_list.py', 'file.txt']
--------------------------------------------------

Found directory: .\uploads #디렉터리를 찾아 다음 순차적으로 돌아간다(재귀)
Subdir: []
File: ['03_print.py']

"""
