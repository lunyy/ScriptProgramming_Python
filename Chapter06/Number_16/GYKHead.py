import turtle
import math
import random

def drawPolygon(x = 0 , y = 0 , radius = 50, numberOfsides = 3) : # 정다각형 그리는 함수
	theta = 360 / numberOfsides # 외각의 크기 이용
	size = 2 * radius * math.sin(math.radians(theta / 2)) # 변의 길이를 결정 : 2rsin(theta/2)
	turtle.penup()
	turtle.goto(x,y)
	turtle.goto(x,y+radius)
	turtle.pendown()
	for i in range(0,numberOfsides) : # 다각형의 변의 개수만큼 loop 돌리기
		turtle.right(theta) # 외각의 크기만큼 반대로 각도 꺾기 -> 내각의 크기만큼 꺾게 됨
		turtle.forward(size) # 변의 길이만큼 그리기
		
def rollDice(): # 주사위 굴리기
	return random.randrange(1,7)
	
def playCraps(): # Craps 게임을 구현한 함수
	turn1 = rollDice()
	turn2 = rollDice()
	#print("Dice : ", turn1, ", ", turn2 , " => " , turn1 + turn2)
	if (turn1 + turn2 == 2) or (turn1 + turn2 == 3) or (turn1 + turn2 == 12) : # 2,3,12가 나오면 패배
		return 0
	elif (turn1 + turn2 == 7) or (turn1 + turn2 == 11) :# 7,11이 나오면 승리
		return 1
	else : 
		point = turn1 + turn2 # 인자를 만들어 놓고
		#print(point,"점입니다.")
		while True :
			flag = extraGame(point) # extraGame에 넣음
			if flag == 0 : # flag를 받아와서 0이면 패배
				return 0
			elif flag == 1 : # 1이면 승리
				return 1

def extraGame(point): # 예외수가 되지 않은 경우
	turn1 = rollDice()
	turn2 = rollDice()
	#print("Dice : ", turn1, ", ", turn2 , " => " , turn1 + turn2)
	if (turn1 + turn2 == 7) : # 7이 되면 패배
		return 0
	elif (turn1 + turn2 == point) : # 같은 점수가 되면 승리
		return 1
		
def isValid(side1,side2,side3): # 삼각형의 성립조건을 판별하는 함수
	if (side1 + side2) > side3 :
		if (side1 + side3) > side2 :
			if (side2 + side3) > side1 :
				return True
			else :
				return False
		else :
			return False
	else :
		return False
	
def area(side1,side2,side3) : # 삼각형의 면적을 구하는 함수
	s = side1 + side2 + side3 # 모든 변을 더해 저장한 s
	t_area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3)) # 세 변의 길이를 알 때 사용할 수 있는 삼각형의 넓이 공식
	return t_area
	
def findMersenne (num) : # Mersenne Prime을 찾는 함수
	if isPrimeNumber(2**num-1) == True : # 소수 판별기
		return 2 ** num - 1 # 만약 소수면 return True
	else :
		return False # 아니면 return False
	
	
def isPrimeNumber(number): # 소수인지를 판별
	for i in range(2,int(math.sqrt(number)) + 1): 
		if number % i == 0: # 2~sqrt(number)+1까지의 수 중 나누어 떨어지는 수가 있다면
			return False # 소수가 아님
	return True # 나머진 소수.
	
def convertMillis(millis): # 밀리세컨드 -> 시 / 분 / 초
	seconds = int(millis / 1000) # 초를 입력받아 1000으로 나눔 -> 전체 초
	minutes = int(seconds / 60) # 전체 초를 60으로 나눔 -> 전체 분
	hours	= int(minutes / 60) # 전체 분을 60으로 나눔 -> 전체 시
	seconds = seconds % 60 # 60의 나머지 연산으로 시를 구함
	minutes = minutes % 60 # 60의 나머지 연산으로 분을 구함
	print(hours, " : ", minutes, " : ", seconds) # 출력
	 
def numberOfDaysInYear(year): # Number 16 
	if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) : # 윤년이면
		return 366 # 366일
	else : #나머지는
		return 365 # 365일
