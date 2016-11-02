def prefix(s1,s2):
	retstr = "" # 기본 문자열을 빈 문자열로 설정
	if (len(s1) > len(s2)) :
		length = len(s2) 
	else :
		length = len(s1)
	#문자열 길이 초과 방지를 위해 가장 짧은 문자열을 기준으로 설정
	for i in range (0,length) :
		if (s1[i] == s2[i]):
			retstr = retstr + s1[i]
		#같은 문자가 있다면 문자열에 저장.
		if (s1[i] != s2[i]) :
			break
		# 다른 문자가 생기면 바로 break
	return retstr # 더한 문자열 리턴
	
def main():
	print("Enter String 01 : ",end="")
	s1 = input()
	print("Enter String 02 : ",end="")
	s2 = input()
	#문자열 입력 받기
	ret = prefix(s1,s2)
	print(ret)
	
main()