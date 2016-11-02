import turtle


window = turtle.Screen()
window.bgcolor('lightblue') # 바탕화면 설정


Cb = turtle.Turtle()
Cb.speed(0) # 빠른 그림 (0 : Fastest)

#하나의 사각형을 그리고 채우기.
def square (size,alternate,color):
	Cb.color(color) # 내부에 채울 색 설정
	Cb.begin_fill() # 내부 색 채우기
	for i in range(4): # 사각형 그리기
		Cb.forward(size) # 변의 길이만큼 그리기
		Cb.left(90)	# 좌로 90도 돌기
	Cb.end_fill()  	# 색 채우기 종료
	Cb.forward(size)# 변의 길이만큼 앞으로 가기.
	
#한 줄의 사각형을 그리기.
def row(size,alternate,color1,color2):
	for i in range(4):
		if(alternate == True):	# 첫 줄의 타일 색 타입
			square(size,alternate,color1)
			square(size,alternate,color2)
		else:					# 둘째 줄의 타일 색 타입
			square(size,alternate,color2)
			square(size,alternate,color1)
		
#체스보드 사각형 전체 그리기
def chessboard(size,alternate,color1,color2):
	Cb.penup()
	Cb.goto(-(size * 4),(size * 4)) # 시작지점으로 이동
	for i in range(8):
		row(size,alternate,color1,color2)	# 한 줄씩 그려나가기
		Cb.back(size * 8) 
		Cb.right(90)
		Cb.forward(size)
		Cb.left(90)							# 다음 줄 첫 지점으로 이동
		if (alternate == True):				# [
			alternate = False				# |교차 Flag
		else :								# |
			alternate = True				# [
	input()

chessboard(50,True,'white','black')			# 함수 실행	
