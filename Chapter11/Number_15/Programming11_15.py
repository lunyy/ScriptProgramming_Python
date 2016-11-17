def isSameLine(points):
	firstslope = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0]) 
	#초기 기울기 지정.
	for i in range(0,len(points)):
		for j in range(i + 1,len(points)):
			if (points[j][0] != points[i][0]):
			    if firstslope != (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) :
			        return False
			else : 
				return False
	#같은 기울기인가 + 같은 직선상에 있는가를 검사.
	return True

def main():
	print("다섯 개의 점을 입력하세요 : ")
	string = input()
	temp = [eval(x) for x in string.split()]
	points01 = [[temp[0],temp[1]],[temp[2],temp[3]],[temp[4],temp[5]],[temp[6],temp[7]],[temp[8],temp[9]]]
	# 사용자 입력
	if isSameLine(points01) :
		print("해당 점들은 같은 직선 위에 있습니다.")
	else :
		print("해당 점들은 같은 직선 위에 없습니다.")

main()