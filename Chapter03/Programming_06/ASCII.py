print("아스키 코드를 입력하세요")
char = eval(input()) # 아스키 코드 입력받기 (정수로)

char = chr(char) # chr 함수를 통해 파라미터에 해당하는 정수 값을 아스키 문자로 변환

print("문자는 ", char , " 입니다.")

