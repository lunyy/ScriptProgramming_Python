print("Enter integer : ")
integerInput = eval(input()) # 정수 입력받기.

posNum1 = integerInput % 10 # 일의 자릿수 계산 
posNum10 = (integerInput % 100) // 10 # 십의 자릿수 계산
posNum100 = (integerInput % 1000) // 100 # 백의 자릿수 계산
posNum1000 = integerInput // 1000 # 천의 자릿수 계산

print (posNum1000 , posNum100 , posNum10 , posNum1) # 각 숫자 출력