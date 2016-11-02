import turtle
import math

print("Enter point01 : ")# p0
point01_x = eval(input())
point01_y = eval(input())

print("Enter point02 : ")# p1
point02_x = eval(input())
point02_y = eval(input())

print("Enter point03 : ")# p2
point03_x = eval(input())
point03_y = eval(input())

turtle.penup()
turtle.goto(point01_x,point01_y)
turtle.pendown()
turtle.goto(point02_x,point02_y)
turtle.penup()
# 선분 p0 - p1 그리기
turtle.goto(point03_x,point03_y)
turtle.pendown()
# 점 p2 찍기

if ((point02_x - point01_x) * (point03_y - point01_y) - (point03_x - point01_x) * (point02_y - point01_y)) > 0 : 
	turtle.write("p2는 직선의 왼쪽에 있습니다.")
elif ((point02_x - point01_x) * (point03_y - point01_y) - (point03_x - point01_x) * (point02_y - point01_y)) == 0 :
	turtle.write("p2는 직선에 포함되어 있습니다.")
elif ((point02_x - point01_x) * (point03_y - point01_y) - (point03_x - point01_x) * (point02_y - point01_y)) < 0 :
	turtle.write("p2는 직선의 오른쪽에 있습니다.")
	
# 판별하기 위한 식이 교과서에 첨부됨.
input()