def main():
	print("Enter number of cities : ")
	#num = eval(input())
	num = 5
	print("Enter position of cities : ")
	mystr = input()
	mylist = mystr.split()
	point = []
	for i in range(0,len(mylist),2) :
		point.append([eval(mylist[i]),eval(mylist[i+1])]) 
	pos = nearestPoints(point)
	print("Center city is in ", point[pos])
def distance(x1,y1,x2,y2):
	return ((x2-x1)**2 + (y2-y1)**2)**0.5

def nearestPoints(points):
	centercitylist = []
	mysum = 0
	p1 = 0
	for i in range(0,len(points)):
		mysum = 0
		for j in range(0,len(points)):
			mysum += (distance(points[i][0],points[i][1],points[j][0],points[j][1]))
		centercitylist.append(mysum)
		if centercitylist[p1] > centercitylist[i] :
			p1 = i
	return p1

main()