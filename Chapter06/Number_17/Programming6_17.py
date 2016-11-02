import GYKHead

def main():	
	print("삼각형의 세 변을 입력하시오 : ")
	a = eval(input())
	b = eval(input())
	c = eval(input())
	if GYKHead.isValid(a,b,c) :
		print("삼각형의 넓이는 : ", round(GYKHead.area(a,b,c),3) , "입니다.")
	else :
		print("Invalid input!")
		
main()