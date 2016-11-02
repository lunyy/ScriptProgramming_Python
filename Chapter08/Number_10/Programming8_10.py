from decimalToBinary import decimalToBinary

def main():
	print("Enter Decimal : ", end="")
	value = input()
	list = decimalToBinary(value)
	for i in range(0,len(list)):
		print(list[i],end="") # 리스트의 값을 하나씩 출력해 냄.
	print("")

main()