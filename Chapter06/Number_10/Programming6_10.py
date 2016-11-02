def isPrimeNumber(number): # 소수인지를 판별
	for i in range(2,number): 
		if number % i == 0: # 2~number-1까지의 수 중 나누어 떨어지는 수가 있다면
			return False # 소수가 아님
	return True # 나머진 소수.

print("Enter Input : ",end="") 
number = eval(input())
if	number != 1 and number != 2 and isPrimeNumber(number) == True : # 1은 소수가 아니므로 제외
	print(number,"is prime number ") # 소수인 경우 소수라고 출력
elif number == 2: # 2는 특별한 소수
	print("2 is prime number ")
elif number == 1 or isPrimeNumber(number) == False: # 소수가 아닌 경우
	print(number, "is not prime number") # 소수가 아님.