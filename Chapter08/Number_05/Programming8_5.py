from countFunc import countFunc
	
def main():
	print("Enter String : ")
	s1 = input()
	print("Enter substring : ")
	s2 = input()
	# 문자열 입력
	print("The number that string includes substring is : " , countFunc(s1,s2))
	# count 함수를 이용하여(substring이 나오는 빈도를 알려주는 내장함수) 값을 구함.
	
main()