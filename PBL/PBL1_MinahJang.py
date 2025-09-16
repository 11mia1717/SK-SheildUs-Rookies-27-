import random

def play_game():
    #게임을 실행하는 함수

    #게임 화면 출력
    print("===========숫자맞추기 게임(1부터 100까지)=========")
    print("컴퓨터가 1부터 100사이의 숫자를 생각합니다")
    print("Player는 컴퓨터가 생각한 숫자를 맞춰주세요")
    print("="*50)

    print("컴퓨터가 숫자를 생각하고 있습니다.....")
    #컴퓨터가 랜덤하게 생각한 숫자(1~100 범위)
    computer_number = random.randint(1, 100)
    #문제맞추기를 시도한 횟수를 세는 변수 정의
    count = 0 

    #게임을 위한 반복문
    while True:
        try :
            #Player가 숫자를 맞추는 구문
            player_number = int(input("숫자를 맞춰주세요 : ")) 
            # 숫자 입력 범위 체크
            if player_number < 1 or player_number > 100:
                print("1부터 100까지의 숫자를 입력해주세요.")
                continue

            #문제 맞추기를 시도한 회수 증가
            count += 1
            #Player가 생각한 숫자와 컴퓨터의 숫자가 일치하는 경우
            if player_number == computer_number:
                print(f"축하합니다!!!!!!! {count}번만에 맞추셨군요!")
                print(f"숫자 {player_number}은(는) 컴퓨터가 생각한 숫자와 정확히 일치합니다.")
                break
                    
            #Player가 생각한 숫자가 컴퓨터의 숫자보다 작은 경우
            elif(player_number < computer_number):
                print(f"다시 시도해보세요. 숫자 {player_number}는 제가 생각한 숫자보다 작습니다.")
                            
            #Player가 생각한 숫자가 컴퓨터의 숫자보다 큰 경우 
            else:
                print(f"다시 시도해보세요. 숫자 {player_number}는 제가 생각한 숫자보다 큽니다.")
        #숫자 외 입력에 대한 에러 처리    
        except ValueError:
            print("숫자만 입력해주세요!!")
            continue                                                                        

def main():
    while True:
        #게임 실행 함수 호출
        play_game()      
        #재 게임 여부 붇기
        regame = input("게임을 다시 하시겠습니까? (Y/N): ").strip().lower()
        if regame != "y":
            print("게임이 종료됩니다. 감사합니다!")
            break   
        
if __name__ == "__main__":
    #게임 시작 메인함수를 호출    
    main()            