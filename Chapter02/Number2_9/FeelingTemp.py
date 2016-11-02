print("화씨 -58도에서 41도 사이의 온도를 입력하십시오 : ")
far_temp = eval(input()) # 화씨 온도 입력

print("풍속을 시간당 마일 단위로 입력하십시오 : ")
mile = eval(input()) # 풍속 입력

feel_temp = 35.74 + 0.6215 * far_temp - 35.75 * (mile ** 0.16) + 0.4275 * far_temp * (mile ** 0.16) #공식을 이용하여 계산하기
feel_temp = round(feel_temp,6) # 출력 양식에 맞게 반올림.
print("체감온도는 " , feel_temp , "입니다.")