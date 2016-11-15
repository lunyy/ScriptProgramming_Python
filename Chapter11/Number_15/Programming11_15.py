def isSameLine(points):
	firstslope = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0]) 
	for i in range(0,len(points)):
		for j in range(i + 1,len(points)):
			if (points[j][0] != points[i][0]):
			    if firstslope != (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) :
			        return False
			else : 
				return False
	return True

def main():
	#points01 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
	#points02 = [[3.4,2],[6.5,11.5],[2.3,2.3],[5.5,5],[-5,4]] 
	print("다섯 개의 점을 입력하세요 : ")
	string = input()
	temp = [eval(x) for x in string.split()]
	points01 = [[temp[0],temp[1]],[temp[2],temp[3]],[temp[4],temp[5]],[temp[6],temp[7]],[temp[8],temp[9]]]
	if isSameLine(points01) :
		print("points01 은 같은 직선 위에 있습니다.")
	else :
		print("points01 은 같은 직선 위에 없습니다.")

main()