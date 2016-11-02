print("년과 1월 1일의 요일을 입력하십시오 : ") # 년과 그 해의 첫 날을 입력받음
year = eval(input())
getfirstday = eval(input())
yearFlag = 0 # 윤년인가?
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 : # 윤년이면
	yearFlag = 1 # 윤년 상태 ON

for i in range(1,13) :
	print()# 달력의 틀 출력
	print("			",year,"년 ",i,"월")
	print("======================================================")
	print("일	월	화	수	목	금	토")
	cnt = 1 # cnt는 다음 달의 첫 날을 설정하기 위한 변수
	if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12) : # 31일인 달
		for j in range (0,getfirstday + 1) : # 첫 날 전까지는 공백 출력
			print("",end = "	")
			cnt = cnt + 1
		for j in range (getfirstday, getfirstday + 31) : # 첫 날부터 31일까지 출력
			if cnt % 7 == 0 : # 한 라인당 7일 출력, 토요일이 되면 띄워주기
				print(j-getfirstday + 1 ) 
				cnt = cnt + 1
			else : 
				print(j-getfirstday + 1, end = "	")
				cnt = cnt + 1
		getfirstday = cnt % 7 - 2 # 다음 달의 첫 날 조정
		if getfirstday == -2 :
			getfirstday = 5
	elif (i == 2 and yearFlag == 0) : # 윤년이 아닌 2월
		for j in range (0,getfirstday + 1) :
			print("",end = "	")
			cnt = cnt + 1
		for j in range (getfirstday, getfirstday + 28) : # 28일까지 출력
			if cnt % 7 == 0 :
				print(j-getfirstday + 1 )
				cnt = cnt + 1
			else :
				print(j-getfirstday + 1, end = "	")
				cnt = cnt + 1
		getfirstday = cnt % 7 - 2
		if getfirstday == -2 :
			getfirstday = 5
	elif (i == 2 and yearFlag == 1) : # 윤년인 2월
		for j in range (0,getfirstday + 1) : 
			print("",end = "	")
			cnt = cnt + 1
		for j in range (getfirstday, getfirstday + 29) : # 29일까지 출력
			if cnt % 7 == 0 :
				print(j-getfirstday + 1 )
				cnt = cnt + 1
			else :
				print(j-getfirstday + 1, end = "	")
				cnt = cnt + 1
		getfirstday = cnt % 7 - 2
		if getfirstday == -2 :
			getfirstday = 5
	else : # 30일인 달
		for j in range (0,getfirstday + 1) :
			print("",end = "	")
			cnt = cnt + 1
		for j in range (getfirstday, getfirstday + 30) : # 30일까지 출력
			if cnt % 7 == 0 :
				print(j-getfirstday + 1 )
				cnt = cnt + 1
			else :
				print(j-getfirstday + 1, end = "	")
				cnt = cnt + 1
		getfirstday = cnt % 7 - 2
		if getfirstday == -2 :
			getfirstday = 5
			
print() # 한줄 띄우기.