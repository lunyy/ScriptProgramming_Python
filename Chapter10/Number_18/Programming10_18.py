import os
CONST_SIZE = 8
CONST_ROWS = CONST_SIZE
CONST_COLS = CONST_SIZE
g_solution = [] # Save Solutions
g_index = 0
g_count = 0

def main() :
	global CONST_SIZE
	print("N * Queen Puzzle")
	setNext([])

def checkQueenConflict(list,rows,cols) : # Cheek Queen Conflict.
	for(list_rows,list_cols) in list :
		if list_rows == rows or list_cols == cols or (abs(list_rows - rows) == abs(list_cols - cols)) : # return True if other queen is on this queen's way
			return True
	return False
	
def setQueen(list) : # Set Queen's Position
	retlist = []
	queen_last = [0,0] 
	if not (len(list) == 0) : # set queen_last(likely using stack)
		queen_last = list[-1]
	else : # list initialize
		retlist.append([0,0])
	for i in range(queen_last[0], CONST_ROWS) : # height check(rows)
		for j in range(CONST_COLS) : # width check(cols)
			if i == queen_last[0] and j <= queen_last[1] : # check conflict
				continue
			if checkQueenConflict(list,i,j) == False : # check Conflict
				retlist.append([i,j]) #if they don't conflict -> save position
	return retlist
	
def setNext(list) : # Event Handler
	if len(list) == CONST_SIZE: 
		g_solution.append(list) # append solution to solutionlist
		printSolutions()  # print
	else : 
		nextQueen = setQueen(list) # set next queen position
		while len(nextQueen) != 0: 
			Nowqueen = nextQueen.pop(0) # find new Queen position
			queen_copy = list[:] 
			queen_copy.append(Nowqueen) # input new position to list
			setNext(queen_copy) # do it until solution list's length is CONST_SIZE

def printSolutions() : # print
	global g_index
	global g_count
	os.system("cls")
	k = 0
	for i in range(0,CONST_ROWS) :
		for j in range(0,CONST_COLS) :
			if i == g_solution[g_index][k][0] and j == g_solution[g_index][k][1] : 
				print("Q",end = " |")
				k = (k + 1)%CONST_SIZE
			else :
				print(" ", end = " |")
		print("")
	g_index = g_index + 1
	print("Num of Solutions : ",g_count)
	a = input()
	g_count = g_count + 1
	
main()