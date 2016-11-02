maxnumber = 0
maxcount = 0

while True : # 무한루프
	print("숫자를 입력하세요, 0은 입력 종료 : ", end = "") # 입력 요청
	numinput = eval(input()) # 입력 받기
	if (numinput == 0) : # input이 0이면 종료
		break
	if maxnumber < numinput : # max가 바뀌면 
		maxnumber = numinput # 최대값을 바꾸기.
		maxcount = 0 # count 초기화
	if numinput == maxnumber : # max가 입력되면
		maxcount = maxcount + 1 # 카운트 증가.

print("가장 큰 수는 ", maxnumber ," 입니다.")
print("가장 큰 수가 등장한 빈도는 ",maxcount ," 입니다.")
