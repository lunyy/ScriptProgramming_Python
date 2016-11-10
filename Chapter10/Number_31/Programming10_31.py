def main():
	print("Enter numeric Strings : ",end = "")
	string = input() # get input
	while(string.isnumeric() != True) :
		print("Wrong input. Enter correct numeric Strings : ",end = "")
		string = input()
	# check string valid
	list = count(string)
	for i in range(0,len(list)): # print list
		print(list[i])
	
def count(string): # count numbers
	list = [] # list created
	count = [0 for _ in range(0,10)] # init count list
	for i in range(0,len(string)): 
		for j in range(0,10):
			if eval(string[i]) == j : # check char
				count[j] = count[j] + 1
				break
	for i in range(0,10):
		outputstr = str(i) + " - " + str(count[i]) + "	times were counted" # make string
		list.append(outputstr) # input string to list
		
	return list
	
	
main()
	