import math

print("오각형의 한 변의 길이를 입력하세요")
s = eval(input())#한 변의 길이 입력받기

area = 5 * s * s / (4 * math.tan(math.pi / 5))# 넓이 공식 적용

print("오각형의 넓이는 " , area , " 입니다")