def binaryToDec(binaryValue):
	sum = 0
	#return int(binaryValue,2)
	for i in range(0,len(binaryValue)) :
		sum = sum + eval(binaryValue[i]) * (2 **(len(binaryValue) - i))
		# 기존 값에 1 or 0 (자릿수) * 2^자릿수를 더함.
	return round(sum / 2) 