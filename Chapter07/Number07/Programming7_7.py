from LinearEquation import LinearEquation

def main():
	eq1 = LinearEquation(9,4,3,-5,-6,-21)
	eq2 = LinearEquation(1,2,2,4,4,5)
	# 프로그래밍 4.3의 실행 예시로 테스트
	if eq1.isSolvable() : # 판별식이 0보다 크거나 같다면
		print("EQ1 : ",eq1.getX(), " , " , eq1.getY())
	else : # 그 경우가 아니면
		print("EQ1 : 이 방정식은 해가 없습니다.")
	if eq2.isSolvable() : # 역시 판별식이 0보다 크거나 같다면
		print("EQ2 : ",eq2.getX(), " , " , eq2.getY())
	else : # 그 경우가 아니면
		print("EQ2 : 이 방정식은 해가 없습니다.")
		
main()