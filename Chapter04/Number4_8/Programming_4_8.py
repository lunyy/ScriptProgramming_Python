print("Enter 3 integerws : ") #3개의 정수 입력
a = eval(input())
b = eval(input())
c = eval(input())

if a < b : 
	if a < c:
		if b < c: # c>b>a
			print("[",a,b,c,"]")
		elif b > c: # c>a>b
			print("[",a,c,b,"]")
	elif a > c: # b>a>c
		print("[",c,a,b,"]")
elif b < a: 
	if b < c:
		if a < c: # c>a>b
			print("[",b,a,c,"]")
		else: # a>c>b
			print("[",b,c,a,"]")
	else : # a>b>c
		print("[",c,b,a,"]")
		
list = [a,b,c] # 검사를 위한 리스트의 정렬함수 이용
list.sort()
print(list)