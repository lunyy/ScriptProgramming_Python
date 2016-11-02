import math

print("10개의 숫자를 입력하세요")# 숫자 입력

input01 = eval(input())	
input02 = eval(input())
input03 = eval(input())
input04 = eval(input())
input05 = eval(input())
input06 = eval(input())
input07 = eval(input())
input08 = eval(input())
input09 = eval(input())
input10 = eval(input())

avg = (input01 + input02 + input03 + input04 + input05 + input06 + input07 + input08 + input09 + input10) / 10 # 평균 구하기
sig = (input01**2 + input02**2 + input03**2 + input04**2 + input05**2 + input06**2 + input07**2 + input08**2 + input09**2 + input10**2) # 제곱한 값들의 Sigma
var = math.sqrt((sig - ((avg * 10)**2 / 10)) / 9) #표준편차 구하기
avg = round(avg,6)
var = round(var,6)
print("평균은 ",avg,"입니다.")
print("표준 편차는 ",var, "입니다.")