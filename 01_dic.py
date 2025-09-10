#정해진 키값이 있다면 딕셔너리 방식.
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])

person = {"name": "Mia", "age": 30, "city": "New York"}
print(person.get("name", 0)) 
# get()메서드 : name이라는 값을 찾아서 값이 없으면 0, 잇으면 출력

print(person.keys()) #왼쪽에 잇는 키값만 
print(person.values()) #오른쪽에 잇는 value 값만
print(person.items()) #둘다