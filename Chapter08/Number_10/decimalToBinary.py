def decimalToBinary(value):
	value = eval((value))
	str_list = []
	while(1) :
		if value == 0:
			str_list.append(0)
			break
		elif value == 1:
			str_list.append(1)
			break
		# 0이나 1이면 맨 마지막에 0,1을 넣고 break
		else :
			str_list.append(value % 2)
			value = round(value / 2)
		# 다른 수이면 2로 나눈 나머지를 append하고 value를 2로 나눈 후 continue
	
	return str_list[::-1]