from Fan import Fan

def main():
	fan1 = Fan(Fan.CONST_SLOW,True,10,"Yellow")
	fan2 = Fan(Fan.CONST_MEDIUM,False,5,"Blue")
	#생성자를 이용한 Fan 생성
	print("------------------------Fan1------------------------")
	print("Speed : ",fan1.getSpeed())
	print("On/Off : ",fan1.getisOn())
	print("Radius : ",fan1.getRadius())
	print("Color : ",fan1.getColor())
	#Fan1 테스트
	print("------------------------Fan2------------------------")
	print("Speed : ",fan2.getSpeed())
	print("On/Off : ",fan2.getisOn())
	print("Radius : ",fan2.getRadius())
	print("Color : ",fan2.getColor())
	#Fan2 테스트
	
main()