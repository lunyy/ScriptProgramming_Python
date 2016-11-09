def main():
	print("숫자를 입력하세요.")
	str = input()
	items = str.split()
	list2 = [eval(x) for x in items]
	list1 = list()
	
	printflag = 0
	list1.append(list2[0]) # 첫 숫자는 중복 예외 -> 출력.
	
	for i in range(0,len(list2)):
		for j in range(0,i):
			if list2[i] == list2[j] : # 중복되는게 있다면 출력 안함.
				printflag = 0
				break
			printflag = 1 # 출력 상태 On
		if printflag == 1 : # 출력 On -> 출력
			list1.append(list2[i])
	list1.sort()
	print(list1)
			
				
main()