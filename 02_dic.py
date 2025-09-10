menus = {"아메리카노" : 4000, "카페라떼" : 4500, "카푸치노" : 5000}
#API를 이용하면 위의 방식으로 가져옴


print("===================== 메뉴판 =====================")
for menu, price in menus.items():
    #emulate도 인덱스랑 밸류를 가져오듯이 items도 마찬가지다.
    print(f"{menu} : {price}원")
print("=" * 50)


selected_menu = input("=== 메뉴를 선택하세요. : ")
money = int(input("=== 금액을 입력하세요. : "))

# 메뉴를 선택하고, 거스름 돈을 출력하는 기능을 구현하라
# get() 함수 사용해도 좋음
price = menus.get(selected_menu,0)
if price == 0:
    print("메뉴가 없습니다.")

else :
    change = money - price
    if change >= 0:
        print(f"{selected_menu}를 선택했습니다. 거스름돈은 {change}원 입니다.")
    else :
        print("돈이 부족합니다.")



"""
내 답변;;
change = money-(menus.get(selected_menu, "메뉴를 다시 입력해주세요"))
if change < 0:
    print("금액이 부족합니다.") 

else :
    print(f"거스름돈 {change}원 입니다. 감사합니다.")
    print("=" * 50)
"""