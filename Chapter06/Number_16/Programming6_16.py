import GYKHead
def main():		
	print("2010년에서 2020년까지 총 일수를 출력하는 테스트 프로그램.")
	sum = 0
	for i in range(2010,2021) :
		sum = sum + GYKHead.numberOfDaysInYear(i)
	print("2010년에서 2020년까지 총 일수는 ", sum ,"일 입니다.")
	
main()