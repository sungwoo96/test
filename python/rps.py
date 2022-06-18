# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1 = 가위
# 2 = 바위
# 3 = 보

# 종료 조건: 졌을 때 "졌습니다." 를 출력하고 종료하기

def main(): # main 함수의 시작부분
    computer_rps = 0 # 랜덤 가위바위보를 담아 둘 computer_rps 변수
    user_rps = 0 # 사용자의 가위바위보를 입력받을 user_rps 변수

    print("-----------가위바위보 게임을 시작합니다.------------")
    while(True): # 이기거나 비길때는 반복, 지게 되면 종료하는 무한 루프
        computer_rps = random.randrange(1, 3 + 1) # 1~3 중 하나를 저장
        user_rps = int(input("1. 가위\t2. 바위\t3. 보: ")) # 가위 바위 보 입력받기
        if user_rps != 1 and user_rps != 2 and user_rps != 3: # 유저가 입력한 값이 1~3사이의 값이 아닐 경우 다시 입력받기
            continue
        else:
            if user_rps == computer_rps: # 비겼을 때
                print("비겼습니다.")
            elif user_rps == 1: # 유저가 가위일 때
                if computer_rps == 2: # 컴퓨터가 바위일 때
                    print("졌습니다.")
                    break # 게임 종료
                else: # 컴퓨터가 보일 때
                    print("이겼습니다.")
            elif user_rps == 2: # 유저가 바위일 때
                if computer_rps == 3: # 컴퓨터가 보일 때
                    print("졌습니다.")
                    break # 게임 종료
                else:  # 컴퓨터가 가위일 때
                    print("이겼습니다.")
            elif user_rps == 3: # 유저가 보일 때
                if computer_rps == 1: # 컴퓨터가 가위일 때
                    print("졌습니다.")
                    break  # 게임 종료
                else:  # 컴퓨터가 보일 때
                    print("이겼습니다.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__': # 메인 함수
    main() # main() 함수 호출