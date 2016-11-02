print("년과 월을 입력하십시오 : ") # 년과 열을 입력받음
year = eval(input())
month = eval(input())

if(month == 1): # 1월은 31일
	print(year,"년 ",month,"월은 31일입니다.")
elif(month == 2): # 2월은
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
		print(year,"년",month,"월은 29일입니다.") #윤년은 29일
	else :
		print(year,"년",month,"월은 28입니다.") #윤년이 아니면 28일
elif(month == 3):# 3월은 31일
	print(year,"년",month,"월은 31일입니다.")
elif(month == 4):# 4월은 30일
	print(year,"년",month,"월은 30일입니다.")
elif(month == 5):# 5월은 31일
	print(year,"년",month,"월은 31일입니다.")
elif(month == 6):# 6월은 30일
	print(year,"년",month,"월은 30일입니다.")
elif(month == 7):# 7월은 31일
	print(year,"년",month,"월은 31일입니다.")
elif(month == 8):# 8월은 31일
	print(year,"년",month,"월은 31일입니다.")
elif(month == 9):# 9월은 30일
	print(year,"년",month,"월은 30일입니다.")
elif(month == 10):# 10월은 31일
	print(year,"년",month,"월은 31일입니다.")	
elif(month == 11):# 11월은 30일
	print(year,"년",month,"월은 30일입니다.")
elif(month == 12):# 12월은 31일
	print(year,"년",month,"월은 31일입니다.")	
		