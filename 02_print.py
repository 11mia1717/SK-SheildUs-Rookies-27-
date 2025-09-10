name = input("이름을 입력하세요. : ")
phone = input("전화번호를 입력하세요. : ")
age = input("나이를 입력하세요. : ")
#input은 자동으로 str로 형변환 시켜준다.

print(name)
print(phone)

print(name, "님의 전화번호는", phone, "입니다.", "나이는", age, "세")

print(type(name))
print(type(phone)) #내가 입력한 값들, 전달할 값들을 확인하기 위해
#중간중간 특히, 디버깅용으로 많이 사용하게 됨
#lst, set 등의 형태로 나옴, 거의 lst

print("내 이름은 {}이고 나이는 {}살입니다.".format(name,age))
#format 메서드를 이용하여 자동 포맷팅

print(f"내 이름은 {name}이고 나이는 {age}살입니다.")
#f-string 가장 최신 기능