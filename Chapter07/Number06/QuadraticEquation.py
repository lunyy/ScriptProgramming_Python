import math

class QuadraticEquation :
	def __init__(self, a,b,c):
		self.__a = a
		self.__b = b
		self.__c = c
		# 생성자, 디폴트값은 주지 않음
	def getA(self):
		return self.__a
	def getB(self):
		return self.__b
	def getC(self):
		return self.__c
		# 접근자
	def getDiscriminant(self):
		return ((self.__b * self.__b) - (4 * self.__a * self.__c))
		#판별식 b^2 - 4ac를 리턴해줌.
	def getRoot1(self):
		if ((self.__b * self.__b) - (4 * self.__a * self.__c) >= 0) :
			return round((- self.__b + math.sqrt((self.__b * self.__b) - (4 * self.__a * self.__c))) / (2 * self.__a),6)
		else :
			return 0
		# 판별식을 이용해 근의 공식을 가져옴. + 케이스의 근의 공식
	def getRoot2(self):
		if ((self.__b * self.__b) - (4 * self.__a * self.__c)) :
			return round((- self.__b - math.sqrt((self.__b * self.__b) - (4 * self.__a * self.__c))) / (2 * self.__a),6)
		else :
			return 0
		# 판별식을 이용해 근의 공식을 가져옴. - 케이스의 근의 공식