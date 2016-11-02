import turtle
import math

print("원 A의 좌표와 반지름을 입력하세요 : ") # 원 A에 대한 정보 입력받기
a_x = eval(input())
a_y = eval(input())
a_rad = eval(input())

print("원 B의 좌표와 반지름을 입력하세요 : ") # 원 B에 대한 정보 입력받기
b_x = eval(input())
b_y = eval(input())
b_rad = eval(input())

turtle.penup() # 그림 모드 해제
turtle.goto(a_x,a_y) # 좌표 변경
turtle.pendown() # 그림 모드 - 직선 긋기
turtle.circle(a_rad)  # 원 그리기
turtle.penup() # 그림 모드 해제
turtle.goto(b_x,b_y) # 좌표 변경
turtle.pendown() # 그림 모드 ON
turtle.circle(b_rad) # 원 그리기

centerdistance = math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2) # 중심과 중심 사이의 거리로 판별

if a_rad >= b_rad : # 큰 값과 작은 값 설정을 위한 분기
	bigrad = a_rad 
	smlrad = b_rad
else :	# 큰 값과 작은 값 설정을 위한 분기
	bigrad = b_rad
	smlrad = a_rad

if centerdistance > a_rad + b_rad : # 중점 사이의 거리가 반지름의 합보다 큰 경우 -> 만나지 않는다.
	turtle.write("원 2와 원 1은 겹치지 않습니다")
elif centerdistance == a_rad + b_rad : # 중점 사이의 거리가 반지름의 합과 같은 경우 -> 한 점에서 만난다.
	turtle.write("원 2는 원 1과 한 점에서 만납니다.")
elif centerdistance < a_rad + b_rad : # 중점 사이의 거리가 반지름의 합보다 작은 경우
	if bigrad * 2 < bigrad + smlrad * 2: # 큰 반지름의 2배가 큰 반지름과 작은 반지름의 2배의 합보다 작은 경우 -> 교집합을 이루는 것처럼 보임.
		turtle.write("원 2는 원 1과 겹칩니다.")
	elif bigrad * 2 >= bigrad + smlrad * 2: # 큰 반지름의 2배가 큰 반지름과 작은 반지름의 2배의 합보다 큰 경우 -> 큰 원 내부에 작은 원이 존재함.
		turtle.write("원 2는 원 1 내부에 있습니다.")

input()