import random

def main():
	print("Enter Rows : ")
	rows = eval(input())
	print("Enter Cols : ")
	cols = eval(input())
	print("Enter Matrix: ")
	mystr = input()
	alist = mystr.split()
	mylist = []
	for i in range(0,rows * cols,cols) :
		mylist.append([eval(alist[x]) for x in range(i,i+cols)])
	# User Input
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
				# 수평 성분 검사
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
				# 수직 성분 검사
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
				# 좌측 하단 대각성분 검사
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
				#우측 하단 대각성분 검사.
	return False


main()