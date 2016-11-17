import math

def multiplyMatrix(a,b):
	matrix = [0 for _ in range(0,len(b))] # define matrix list
	cols = [0 for _ in range(0,len(b[0]))] # define colums list
	rows= [0 for _ in range(0,len(b))] # define rows list
	if len(a[0]) == len(b) : # Only can be calculated when number of left matrix's colum and right matrix's row are same
		for i in range(0 ,len(b[0])):
		    cols = [0 for _ in range(0,len(b[0]))] # init cols.
		    for k in range(0,len(a[0])):
		    	for j in range(0,len(a[0])):
		    	    cols[k] += round(a[i][j] * b[j][k],2) #set cols.
		    rows[i] = cols[:] # deep copy
		    matrix[i] = rows[i][:] # copy to ret list
		return matrix
	else :
		return False


def main():
	print("Enter Matrix A : ")
	astr = input()
	alist = astr.split()
	a = []
	for i in range(0,len(alist),(int)(math.sqrt(len(alist)))) :
		a.append([eval(alist[x]) for x in range(i,i+(int)(math.sqrt(len(alist))))])
	print("Enter Matrix B : ")
	bstr = input()
	blist = bstr.split()
	b = []
	for i in range(0,len(blist),(int)(math.sqrt(len(alist)))) :
		b.append([eval(blist[x]) for x in range(i,i+(int)(math.sqrt(len(alist))))])
	# Get UserInput
	matrix = multiplyMatrix(a,b)
	print(matrix)

main()