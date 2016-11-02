print("Enter integer : ")
numberInput = eval(input()) # 정수 입력받기 (입력은 세 자리 정수로 한정)

firstPosNum = numberInput // 100 # 백의 자릿수 계산 - 100으로 정수나누기 연산을 해 소수 떼기

secondPosNum = (numberInput // 10) % 10 # 십의 자릿수 계산 - 일의 자리를 없애고 나머지 연산

thirdPosNum = numberInput % 10 # 일의 자릿수 계산 - 10으로 나머지 연산.

sum = firstPosNum + secondPosNum + thirdPosNum # 전부 더하기
print("Sum of each pos num is : " , sum)

print(firstPosNum, secondPosNum, thirdPosNum)
