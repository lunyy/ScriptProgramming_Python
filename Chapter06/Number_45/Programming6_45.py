import turtle
import math
import GYKHead
	
def main():
	for i in range(3,9) :
		GYKHead.drawPolygon((i - 5) * 100 , 0 , 50 , i)
	input()
	
main()