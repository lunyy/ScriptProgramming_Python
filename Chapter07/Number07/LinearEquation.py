import math

class LinearEquation:
	def __init__(self,a,b,c,d,e,f):
		self.__a = a
		self.__b = b
		self.__c = c
		self.__d = d
		self.__e = e
		self.__f = f
	#생성자 설정 : 각 계수들을 가져옴.
	def getA(self):
		return self.__a
	def getB(self):
		return self.__b
	def getC(self):
		return self.__c
	def getD(self):
		return self.__d
	def getE(self):
		return self.__e
	def getF(self):
		return self.__f
	# 각 계수들의 getter
	def isSolvable(self):
		return (((self.__a * self.__d) - (self.__b * self.__c)) != 0)
	# ad - bc가 0이라면 false, 아니면 true 리턴
	def getX(self):
		return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
	#X값을 구하는 공식을 이용한 리턴
	def getY(self):
		return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
	#Y값을 구하는 공식을 이용한 리턴