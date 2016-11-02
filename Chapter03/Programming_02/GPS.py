import math

print("Press the position of point 1")# 점 1 입력받기.
x1 = eval(input())
y1 = eval(input())

print("Press the position of point 2")# 점 2 입력받기.
x2 = eval(input())
y2 = eval(input())

r = 6370.01#주어진 지구의 평균 반지름

d = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2)))
# d를 구하기 위한 공식 적용. radian을 사용한다고 하였기 때문에 math.radian을 사용하였다.
print("The distance of two points is : " , d) 