def main():
	print("파일명을 입력하세요.",end = " : ")
	filename = input()
    # 파일 이름 get
	f = open(filename,'r')
	txt = f.read()
    # 파일 열기
	print("교체될 이전 문자열을 입력하세요.",end = " : ")
	findstr = input()
    # 교체될 문자열 입력받기
	print("이전 문자열을 대체할 새로운 문자열을 입력하세요.",end = " : ")
	changestr = input()
    # 대체 문자열 입력받기
	txt = txt.replace(findstr,changestr) 
    # string.replace 함수를 이용해 문자열 대체
	f = open(filename,'w')
    # 파일을 읽기 모드로 열기
	f.write(txt)
    # 대체한 문자열을 파일에 출력
	f.close()

main()