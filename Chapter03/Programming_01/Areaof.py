import math

print("Press the distance from center to point")
r = eval(input()) # 입력 받기

s = 2 * r * math.sin(math.pi / 5) # 거리 r이 주어졌으므로, s를 계산하기

area = 3 * math.sqrt(3) / 2 * s * s # s를 구하였으므로, 넓이를 구하기

print("Area is : " , area)