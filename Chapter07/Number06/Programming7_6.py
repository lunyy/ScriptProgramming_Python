from QuadraticEquation import QuadraticEquation

def main():
	qe1 = QuadraticEquation(1,2,1)
	qe2 = QuadraticEquation(1,2,3)
	qe3 = QuadraticEquation(1,3,1)
	# 다항식 생성
	if (qe1.getDiscriminant() > 0) :
		print("QE1 : ", qe1.getRoot1() , " , " ,qe1.getRoot2())
	elif (qe1.getDiscriminant() == 0) :
		print("QE1 : ", qe1.getRoot1())
	elif (qe1.getDiscriminant() < 0) :
		print("QE1 : 해가 없습니다.")
	#QE1에 대한 출력	
	if (qe2.getDiscriminant() > 0) :
		print("QE2 : ", qe2.getRoot1() , " , " ,qe2.getRoot2())
	elif (qe2.getDiscriminant() == 0) :
		print("QE2 : ", qe2.getRoot1())
	elif (qe2.getDiscriminant() < 0) :
		print("QE2 : 해가 없습니다.")
	#QE2에 대한 출력
	if (qe3.getDiscriminant() > 0) :
		print("QE3 : ", qe3.getRoot1() , " , " ,qe3.getRoot2())
	elif (qe3.getDiscriminant() == 0) :
		print("QE3 : ", qe3.getRoot1())
	elif (qe3.getDiscriminant() < 0) :
		print("QE3 : 해가 없습니다.")
	#QE3에 대한 출력
		
main()