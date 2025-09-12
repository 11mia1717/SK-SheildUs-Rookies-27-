#while 반복 while True 사용
#메뉴를 선택한다. (여러개의 메뉴를 선택 한다.)
#구매한 메뉴를 리스트로 보관도 해야 한다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.
#구매했던 리스트와 총 구매가격? 출력!!!

menus = {"아메리카노" : 4000, "카페라떼" : 4500, "카푸치노" : 5000} #딕셔너리

order_list = [] #리스트
total_price = 0

print("===================== 메뉴판 =====================")
for menu, price in menus.items():
    #emulate도 인덱스랑 밸류를 가져오듯이 items도 마찬가지다.
    print(f"{menu} : {price}원")
print("=" * 50)

while True: #무한
    selected_menu = input("주문할 메뉴를 입력하세요(주문종료는 q) : ")
    price = menus.get(selected_menu, 0)

    if price != 0: #0이 아니면 데이터가 있다면
        order_list.append(selected_menu) #끝에 붙이기
        total_price += price
        
    elif selected_menu == "q":
        print("주문 완료.")
        break #while문을 나감

    else :
        print("메뉴가 없습니다. 다시 입력해주세요.")

order_str = ", ".join(order_list)
#join()은 문자열 메서드입니다. <ai
#리스트(또는 다른 반복 가능한 객체) 안의 문자열들을 하나의 문자열로 이어붙일 때 사용 <ai

print(f"{order_str} 주문하셨습니다. 총 {len(order_list)}개 입니다.")
#print(f"주문한 메뉴 : {order_list}")
print(f"총 주문금액은 {total_price}원 입니다.")

while True:
    money = int(input("지불금액을 입력하세요. : "))
    change = money - total_price
   
    if change >= 0:
        print(f"거스름돈은 {change}원 입니다.")
        break
    else :
        print(f"돈이 부족합니다. 다시 지불해주세요.")

print("=" * 50)
"""
# print(f"주문한 메뉴 : {order_list}")
for i, order in enumerate(order_list):
    print(f"{order}")
print(f"총 {i+1}개 주문하셨습니다.")
"""

print(f"{order_str} 주문하셨습니다. (총 {len(order_list)}개)")

print(f"총 주문금액 : {total_price}원")
print(f"지불한 금액 : {money}원")
print(f"거스름돈은 {change}원 입니다. 감사합니다 :)")