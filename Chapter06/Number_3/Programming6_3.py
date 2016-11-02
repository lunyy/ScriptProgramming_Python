def reverse(number): # reverse 함수
	number = number[::-1] # 문자열 슬라이스 : [begin : end : step]를 이용
	return number
	
def isPalindrome(number) : # 대칭수인가?
	if number == reverse(number) : # 만약 뒤집은 것과 동일한 문자열이라면
		return True # True 리턴
	else :
		return False # 아니면 False 리턴
		
print("Input Integer")
number = input()
if isPalindrome(number) == True:
	print("대칭")
else :
	print("대칭 아님")