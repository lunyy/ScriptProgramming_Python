def main():
	mylist = [[4,34],[1,7.5],[4,8.5],[1,-4.5],[1,4.5],[4,6.6]]
	sortedlist = sort_y(mylist)
	print(sortedlist)


def sort_y(mylist):
	y_list = [mylist[i][1] for i in range(0,len(mylist))][:] # y좌표만 따로 집어넣기.
	my_list = list()
	y_list.sort() # 리스트 정렬 함수 사용
	for i in range(0,len(mylist)) :
		for j in range(0,len(mylist)):
			if y_list[i] == mylist[j][1] :
				my_list.append(mylist[j]) # 리스트에 값을 y좌표가 작은 순으로 집어넣기.
	return my_list

main()