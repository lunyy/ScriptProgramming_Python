import math

print("ax^2 + bx + c") # 다항식 입력 형식 표시
print("Enter a : ") # a 입력
a = eval(input())

print("Enter b : ") # b 입력
b = eval(input())

print("Enter c : ") # c 입력
c = eval(input())

if b*b - 4*a*c > 0 : # 만약 판별식이 0보다 크면 
	print("Root is : " , round((-b + math.sqrt(b*b - 4*a*c))/(2*a),6) , " and " , round((b + math.sqrt(b*b - 4*a*c))/(2*a),6)) # 2개의 실근 소수 6자리까지 반올림하여 출력
	
elif b*b - 4*a*c == 0: # 만약 판별식이 0이면
	print("Root is : " , round((-b /(2*a)),6)) # 중근 소수점 6자리까지 반올림하여 출력

elif b*b - 4*a*c < 0: # 만약 판별식이 0보다 작으면
	print("No valid Root exist") # 실근이 존재하지 않음