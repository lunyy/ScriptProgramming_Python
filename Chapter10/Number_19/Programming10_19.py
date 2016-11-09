import random

def main():
	print("Enter Number of balls : ",end = "")
	ballNum = eval(input())
	print("Enter Slots of beanMachine : ",end = "")
	slotNum = eval(input())
	# get input
	slots = [0 for _ in range(0,slotNum)]
	for i in range (0,ballNum) :
		beanMachineSimulate(slots)
	# set slots and paths
	for i in range (ballNum,0,-1) :
		for j in range(0,len(slots)) :
			if slots[j] >= i :
				print("0", end = " ")
			else :
				print(" ", end = " ")
		print()
		
def beanMachineSimulate(slots):
	path = ""
	index = 0
	pins = len(slots) - 1
	for i in range(0,pins) : # pins : triangle / num : slot - 1
		direction = random.randint(0,1) # random direction
		if direction == 0 :
			path = path + "L" # 0 : left
		elif direction == 1:
			path = path + "R" # 1 : right
			index = index + 1  # ball goes to slots[num of right]
	print(path) # path print
	slots[index] = slots[index] + 1 # set slots list
			
main()