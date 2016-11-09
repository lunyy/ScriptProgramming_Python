def main():
	print("Press Any Key to start",end = "")
	buffer = input()
	# Start!
	list = init([])
	list = close(list)
	for i in range(3,101):
		list = reverse(list,i)
		
	print("List of Cabinet are opened")
	for i in range(0,100):
		if list[i] == True:
			print("[",i,"]",end = " ")
	print()
	

def init(list): # open all 
	return list[True for _ in range(0,100)]

def close(list): # close cabinet index multiples of 2
	for i in range(2,100,2):
		list[i] = False
	return list
	
def reverse(list,num): # close cabinet index multibles of num
	for i in range(num,100,num):
		list[i] = not list[i]
	return list