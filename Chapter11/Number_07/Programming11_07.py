def main():
	points = [[-1,0,3],[-1,-1,-1],[4,1,1],[2,0.5,9],[3.5,2,-1],[3,1.5,3],[-1.5,4,2],[5.5,4,-0.5]]
	p1,p2 = nearestPoints(points)
	print("가장 가까운 두 점은 : (" + str(points[p1][0]) + ", " + str(points[p1][1]) + ", " + str(points[p1][2]) + "), (" + str(points[p2][0]) + ", " + str(points[p2][1]) + ", " + str(points[p2][2]) + ")입니다.")


def distance(x1,y1,z1,x2,y2,z2): # 거리 구하는 함수.
	return (((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**0.5

def nearestPoints(points):
	p1,p2 = 0,1

	shortestDistance = distance(points[p1][0],points[p1][1],points[p1][2],points[p2][0],points[p2][1],points[p2][2])
	# 최단 경로를 임의로 지정(선택 정렬 사용)
	for i in range(len(points)) :
		for j in range(i + 1, len(points)):
			d = distance(points[p1][0],points[p1][1],points[p1][2],points[p2][0],points[p2][1],points[p2][2])
		if shortestDistance > d :
			p1,p2 = i,j
			shortestDistance = d
	return p1,p2
	# 선택 정렬을 통한 정렬.
	
main()