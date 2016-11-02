print("총액을 입력하세요 : ")
total = eval(input()) # 총액 입력

print("팁 비율을 입력하세요 : ")
tiprate = eval(input()) # 팁 비율 입력

tip = total * tiprate / 100 # 팁의 액수는 총액 * 팁의 백분율.
total = tip + total  # 총 지불액은 물품의 액수 + 팁

print("팁은 " , tip , "이고 , 총액은 " , total , "입니다")
