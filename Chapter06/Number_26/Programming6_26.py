import math
import GYKHead
	
def main () :
	for i in range (2,32) :
		if GYKHead.isPrimeNumber(i) :
			if GYKHead.findMersenne(i) :
				print("p		2^p-1\n",i,"		",(2**i)-1)
		else :
			continue
			
main()