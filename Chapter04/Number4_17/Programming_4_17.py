import random

com_output = random.randint(0,50000) % 3 # 난수 발생시키기

print("가위(0) 바위(1) 보(2) 중 하나를 입력하십시오 : ") # 사용자 입력
user_input = eval(input())

if com_output == 0 : # 컴퓨터가 가위
	if user_input == 0: # 유저가 가위
		print("DRAW!") # 비김
	elif user_input == 1:# 유저가 바위
		print("YOU WIN!")# 이김
	elif user_input == 2:# 유저가 보
		print("YOU LOSE!")# 패배
	else :
		print("Unvalid Input")# 이상한 입력에 대한 처리
elif com_output == 1 : # 컴퓨터가 바위
	if user_input == 1: # 유저가 바위
		print("DRAW!")# 비김
	elif user_input == 2:# 유저가 보
		print("YOU WIN!")# 이김
	elif user_input == 0:# 유저가 가위
		print("YOU LOSE!")# 패배
	else :
		print("Unvalid Input")# 이상한 입력에 대한 처리
elif com_output == 2 :# 컴퓨터가 보
	if user_input == 2:# 유저가 보
		print("DRAW!")# 비김
	elif user_input == 0:# 유저가 가위
		print("YOU WIN!")# 이김
	elif user_input == 1:# 유저가 바위
		print("YOU LOSE!")# 패배
	else :
		print("Unvalid Input")# 이상한 입력에 대한 처리