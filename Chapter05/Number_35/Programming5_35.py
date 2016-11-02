i = 0
j = 0
sum = 0 # 약수의 합을 저장할 변수
print("완전수는")
for i in range(1,10001): # 1 ~ 10000
	sum = 0
	for j in range(1,i):
		if (i % j) == 0 : # 약수이면
			sum = sum + j # sum에 더하기
	if sum == i : # 약수의 합이 자기 자신과 같으면
		print(i) # 출력
print("입니다.")