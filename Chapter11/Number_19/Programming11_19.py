import random

def main():
	print("Enter Rows : ")
	#rows = eval(input())
	rows = 6
	print("Enter Cols : ")
	#cols = eval(input())
	cols = 7

	mylist = list()
	#for i in range (0,rows) :
	#	mylist.append([random.randint(0,9) for _ in range(0,cols)])
	mylist.append([0,1,0,3,1,6,1])
	mylist.append([0,1,6,8,6,0,1])
	mylist.append([5,6,2,1,8,2,9])
	mylist.append([6,5,6,1,1,9,1])
	mylist.append([1,3,6,1,4,0,7])
	mylist.append([3,3,3,3,4,0,7])
	print(isConsecutiveFour(mylist))
	print("")




def isConsecutiveFour(values):
	rows = len(values)
	cols = len(values[0])
	
	horizMultTarget = 0
	verticMultTarget = 0
	diagonMultTarget = 0
	diagonMultTargetRev = 0

	for i in range(0,rows):
		for j in range(0,cols):
			for k in range(0,4):
				if j + 3 < cols:
					if values[i][j] == values[i][j+k] :
						horizMultTarget += 1
					else :
						horizMultTarget = 0
						break
				else :
					break
			if horizMultTarget == 4:
				return True
			for k in range(0,4):
				if i + 3 < cols :
					if values[i][j] == values[i+k][j] :
						verticMultTarget += 1
					else :
						verticMultTarget = 0
						break
				else :
					break
			if verticMultTarget == 4:
				return True
			for k in range(0,4):
				if i + 3 < rows and j - 3 >= 0:
					if values[i][j] == values[i+k][j-k] :
						diagonMultTarget += 1
					else :
						diagonMultTarget = 0
						break
				else :
					break
			if diagonMultTarget == 4:
				return True
			for k in range(0,4):
				if i + 3 < rows and j + 3 < cols:
					if values[i][j] == values[i+k][j+k] :
						diagonMultTargetRev += 1
					else :
						diagonMultTargetRev = 0
						break
				else :
					break
			if diagonMultTargetRev == 4:
				return True
	return False


main()