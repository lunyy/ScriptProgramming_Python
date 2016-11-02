import math

class RegularPolygon :
	def __init__(self,n = 3,side = 1,x = 0,y = 0) :
		self.__n = n
		self.__side = side
		self.__x = x
		self.__y = y
		#생성자 : 디폴트값을 준, private형 필드를 만들어 내는 생성자.
	def getN(self):
		return self.__n
	def getSide(self):
		return self.__side
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y
		# 접근자
	def setN(self,n):
		self.__n = n
	def setSide(self,side) :
		self.__side = side
	def setX(self,x):
		self.__x = x
	def setY(self,y):
		self.__y = y
		# 설정자
	def getPerimeter(self) :
		return (self.__side * self.__n)
		#둘레값을 반환하여 주는 함수
	def getArea(self) :
		return round((self.__n * self.__side * self.__side / (4 *  math.tan((math.pi / self.__n) ) ) ) ,3)
		# 다각형의 넓이 공식을 이용하여 넓이를 반환하여 주는 함수. 