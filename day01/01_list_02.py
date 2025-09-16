
#리스트 요소 수정
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25  # 두 번째 요소 값을 25로 수정
print(my_list)  # 결과: [10, **25**, 30, 40, 50]

my_list[4] = 100  # 다섯 번째 요소 값을 100으로 수정
print(my_list)  # 결과: [10, 25, 30, 40, 100]4

#리스트 결합
old_list = [5, 6, 7]
new_list = [1, 2, 3, 4]
result = old_list + new_list
print(result)  # 출력: [5, 6, 7, 1, 2, 3, 4]
#차집합 형식일때는 지원이 안된다.
#ex) 기존 데이터에서 다음 데이터에 없는 것을 예외처리를 하고싶다면,
#교집합, 차집합할때는 리스트로 하는게 아니라 set으로 함


#리스트 요소 추가 및 삭제
#바로 출력하는게 아닌, 임시로 데이터를 받아둬야할때
#->append를 사용 항상 제일 마지막에 추가됨.
#굉장히 많이 사용하기 떄문에 기억하자


my_list = [] #리스트 형태로 선언

my_list = [10, 20, 30, 40, 50]
my_list.append(6)  # 리스트 끝에 6 추가
print(my_list)

#인덱스에도 사용한다.
my_list.insert(1, 9)  # 인덱스 1에 9 삽입
print(my_list)

my_list.remove(20)  #데이터를 날린다.
print(my_list)

del my_list[0]  # 첫 번째 인덱스 기준 요소 삭제
print(my_list)