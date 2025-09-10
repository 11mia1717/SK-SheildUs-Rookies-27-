# 아래는 5명의 학생들의 성적을 입력 받아서 
# 최고값, 최소값, 평균값, 90점 이상의 count 프로그램
# 5명의 학생들의 성적을 입력 -> list [] 에 저장

#대문자로 보통 선언함
STUDENTS = 5 #5명의 학생수를 선언
lst = [] #학생들의 성적을 담을 리스트
count = 0 #90점 이상이면 셀 수 있도록

for i in range(STUDENTS): #5번을 돌리겠다.
    #형변환 문자가 들어가면 오류가 발생 int()
    value = int(input(f"{i+1}번째 학생의 성적을 입력하세요. : "))
    lst.append(value) #value 값을 리스트 가장 끝에 담아라

print(f"1등 점수 : {max(lst)}점")
print(f"꼴찌 점수 : {min(lst)}점")
print(f"전체 점수의 합 : {sum(lst)}점")
print(f"평균 점수 : {sum(lst)/len(lst)}점")


for score in lst:
    if score >= 80:
        count += 1  #count = count + 1과 동일

print(f"80점 이상 학생은 {count}명입니다.")


print(f"점수 리스트 : {lst}") 
    