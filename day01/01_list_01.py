fruits = ["사과", "바나나", "오렌지"] 
numbers = [1, 2, 3, 4, 5] #숫자형태의 리스트

print(type(fruits)) #<class 'list' : 대괄호[] 형식의 리스트!
print(fruits)

print(f"과일의 첫번째 : {fruits[0]}")
print(f"과일의 두번째 : {fruits[1]}")
print(f"과일의 세번째 : {fruits[2]}")

#IT지원팀 안에 보안팀!! -> 각팀과 회의를 자주 한다.
#이때 인프라팀은 -증권에 대한 ID, 매수, 매도 얘기를 하면 -> 저장공간DB
#윈도우팀은 -> 레지스트리, 메모리 정보, 하드

#리스트를 임시 저장공간으로 많이 사용한다.

#리스트를 문자열로 한번에 가져오고 싶다면
#포문을 돌려 리스트(fruits)안에 변수(fruit)를 다 가져오겠다
for fruit in fruits: 
    print(f"1. 과일 : {fruit}")

#012로 세번 돌린다. 가져올수 있는 갯수를 정함
#fruits의 index정보를 가져와서 사용하겠다
for i in range(3): 
    print(f"2. 과일 : {fruits[i]}") 

#len이라는 길이 값을 측정해서 가져오겠다.
for i in range(len(fruits)): 
    print(f"3. 과일 : {fruits[i]}") 

#모두 동일한 결과를 보여준다.


##n번째를 표현하고 싶다면
for i in range(len(fruits)): 
    print(f"{i+1}번째 과일 : {fruits[i]}") 
    #i는 0부터 시작하기 때문에 i+1로 표현



#enumerate 함수에 대해서 두개의 값을 반환을 한다
#--Key와 Value값

for i, fruit in enumerate(fruits) :
    print(f"{i+1}번째 과일 : {fruit}")

