print("투자금을 입력하세요 : ")
invMoney = eval(input()) # 투자금 입력

print("연이율을 입력하세요 : ")
powRate = eval(input()) # 연이율 입력

print("년수를 입력하세요 : ")
year = eval(input()) # 년수 입력

valueOfInv = invMoney * ((1 + (powRate / 12 )/100) ** (year*12)) # 연이율을 월이율로 변환 후 공식에 대입
valueOfInv = round(valueOfInv,2) # 출력 양식에 맞게 반올림

print("누적된 가치는 ",valueOfInv,"입니다.")