def main() :
	cnt = 0
	print("Enter Password : ",end = "")
	inputStr = input() # 문자열 input
	if len(inputStr) >= 8 : # 문자열의 길이가 8보다 길면 Correct
		if inputStr.isalnum() : # isalnum : 문자와 숫자로만 구성되었는가 확인
			for i in range(0,len(inputStr)) :
				if (inputStr[i].isnumeric()) : # 숫자의 갯수 세기
					cnt = cnt + 1
			if cnt >= 2 : # 숫자가 2개 이상이면 Correct
				print("Password Created!")
			else : # 숫자가 2개 미만이면 invalid
				print("Invalid Password")
		else : # 문자 / 숫자로만 구성되지 않으면 fail
			print("Invalid Password")
	else : # 문자열의 길이가 8보다 짧으면 Fail
		print("Invalid Password")
	
main()