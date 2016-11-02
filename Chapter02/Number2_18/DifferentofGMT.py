import time # 시간 관련 함수 import

currentTime = time.time() # 현재 시간을 저장

print("GMT와 시간대 차이를 입력하세요 : ")
gmtDiff = eval(input()) # GMT와의 시차 입력

totalSeconds = int(currentTime)

currentSecond = totalSeconds%60

totalMinutes = totalSeconds//60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60 

currentHour = totalHours % 24 + gmtDiff # GMT와의 시차를 보정한 현재 시간.

print("현재 시간은 ",currentHour, ":" , currentMinute, ":", currentSecond,"GMT 입니다.")
