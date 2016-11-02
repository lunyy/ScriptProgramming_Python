from CStock import CStock

def main():
	print("Enter Symbol : ")
	symbol = input()
	print("Enter name : ")
	name = input()
	print("Enter previous closing price : ")
	previousClosingPrice = eval(input())
	print("Enter current price : ")
	currentPrice = eval(input())
	stock = CStock(symbol,name,previousClosingPrice,currentPrice) # 생성자로 입력받은 필드 초기화.
	print("The code of stock is : ", stock.getSymbol())
	print("The name of stock is : ", stock.getName())
	print("The previous closing price of stock is : ", stock.getPreviousClosingPrice())
	print("The current price of stock is : ", stock.getCurrentPrice())
	# 입력받은 필드 출력
	print("set PCP : ")
	pcp = eval(input())
	print("set CP : ")
	cp = eval(input())
	stock.setPreviousClosingPrice(pcp)
	stock.setCurrentPrice(cp)
	# 설정자 테스트
	print("The previous closing price of stock is : ", stock.getPreviousClosingPrice())
	print("The current price of stock is : ", stock.getCurrentPrice())
	print("Change Percent is : " , stock.getChangePercent(),"%")
	

main()