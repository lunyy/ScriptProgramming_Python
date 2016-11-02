
class CStock :
	def __init__(self,symbol = "",name = "", previousClosingPrice = 0,currentPrice = 0) : # 생성자 : symbol,name,price,currentPrice 포함
		self.__symbol = symbol
		self.__name = name
		self.__previousClosingPrice = previousClosingPrice
		self.__currentPrice = currentPrice
		# 전부 private 타입으로 필드 생성
	def getName(self) : 
		return self.__name 
	def getSymbol(self) :
		return self.__symbol
	def getPreviousClosingPrice(self) :
		return self.__previousClosingPrice
		# 접근자
	def setPreviousClosingPrice(self,previousClosingPrice) :
		self.__previousClosingPrice = previousClosingPrice
	def getCurrentPrice(self) :
		return self.__currentPrice
	def setCurrentPrice(self,currentPrice) :
		self.__currentPrice = currentPrice
		# 설정자
	def getChangePercent(self) :
		return round(( ( (self.__currentPrice - self.__previousClosingPrice) / (self.__previousClosingPrice) ) * 100),3)
		# 변화된 비율 반환 -> 변화된 값 / 기존 값 * 100으로 백분율로 표현.
		