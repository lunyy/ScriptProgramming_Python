i = 0
j = 0

for i in range(0,9) :
	for j in range (1,9-i): # 숫자 앞까지의 공백 출력
		print(end = "	")
	for j in range (0,i) : # 숫자 출력 / 공백 출력 ( 0 ~ index : j-1까지)
		print(2**j,end = "	")
	for j in range (i,2*i + 1):# 숫자 출력 / 공백 출력 (j~ index : 2*j까지))
		print(2**(2*i-j) , end = "	")
	print() # 줄 띄우기