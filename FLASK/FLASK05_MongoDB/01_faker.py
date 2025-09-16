from faker import Faker

fake = Faker("ko_KR")

for _ in range(20): #20번 반복한다.
    print(fake.name())    #데이터를 임의적으로 만들 수 있음
    print(fake.address())
    print(fake.email())
    print(fake.phone_number())
    print("="*20)