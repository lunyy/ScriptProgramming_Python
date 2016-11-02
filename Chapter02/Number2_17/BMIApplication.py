print("몸무게를 파운드로 입력하세요 : ")
pound = eval(input()) # 몸무게 입력

print("키를 인치로 입력하세요 : " )
inch = eval(input()) # 키 입력

kilogram = pound * 0.45359237 # | 주어진 변환 비율을 이용한 변환
centimeter = inch * 0.0254    # |

BMI = kilogram / (centimeter ** 2) # BMI 지수 측정 공식 (킬로그램 / cm^2)
BMI = round(BMI,4) # 출력 양식을 위해 반올림

print("BMI지수는 " , BMI , " 입니다")