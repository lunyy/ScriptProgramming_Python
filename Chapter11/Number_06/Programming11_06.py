def multiplyMatrix(a,b):
	matrix = [0 for _ in range(0,len(b))]
	cols = [0 for _ in range(0,len(b[0]))]
	rows= [0 for _ in range(0,len(b))]
	if len(a[0]) == len(b) :
		for k in range(0,len(a)) :
			cols = [0 for _ in range(0,len(b[0]))]
			for i in range(0 ,len(b)):
				for j in range(0,len(b[0])):
					cols[i] += a[i][j] * b[j][i]
				rows[k] = cols[:]
			matrix[k] = rows[k][:]
		return matrix
	else :
		return False


def main():
	a = [[1,1,1],[2,2,2],[3,3,3]]
	b = [[1,1,1],[2,2,2],[3,3,3]]	
	matrix = multiplyMatrix(a,b)
	print(matrix)

main()