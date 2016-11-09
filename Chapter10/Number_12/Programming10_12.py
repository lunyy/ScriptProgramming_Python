def main():
	print("Enter N")
	str = input()
	items = str.split()
	list = [eval(x) for x in items]
	print(gcd(list))
	
def gcd(list):
	list.sort() # 리스트 정렬
	gcdNum = list[0] # 최소값 지정
	n = len(list) # 길이 설정
	for i in range(0,n): 
		remain = list[i] % gcdNum # 유클리드 호제법 사용 -> 큰 수 % 작은 수
		if remain == 0: # 만약 그 것이 최대공약수이면
			list[i] = gcdNum  # 리스트에 그 값을 넣기
		else : # 그 것이 아니라면 
			list[i] = remain # remain을 리스트에 넣기
	if check_gcd(list,gcdNum) == True : # 리스트 검사
		return gcdNum # 최대공약수 리턴
	else : 
		return gcd(list) # 아니라면 재귀.

	
def check_gcd(list,min):
	list.sort()
	for i in range(0,len(list)): # 만약 리스트의 모든 값이 최대공약수라면
		if min != list[i] :
			return False
	return True # 참을 리턴
		
	
main()
	