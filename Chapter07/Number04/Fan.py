class Fan :
	CONST_SLOW = 1
	CONST_MEDIUM = 2
	CONST_FAST = 3
	# 파이썬은 상수 설정이 안 된다..
	def __init__(self,speed = CONST_SLOW,on = False,radius = 5,color = "blue") :
		self.__speed = speed
		self.__on = on
		self.__radius = radius
		self.__color = color
		# 생성자 - 모든 변수 초기화, 문제에서 제시한 디폴트 값을 적용함.
	def getSpeed(self) :
		return self.__speed
	def getisOn(self) :
		return self.__on
	def getRadius(self):
		return self.__radius
	def getColor(self):
		return self.__color
		# getter
	def setSpeed(self,speed) :
		self.__speed = speed
	def setisOn(self,on) :
		self.__on = on
	def setRadius(self,radius):
		self.__radius = radius
	def setColor(self,color):
		self.__color = color
		# setter
	