def sosoo(): #소수 구하는 프로그램
	for k in range(2,11) : # 2~10000사이를 반복
		
		for i in range(2, k+1) :
		
			if k % i == 0: # 2와 자기 자신 사이에 나눠지는 것 있으면 break
				break
		print(k,"는 소수") # 없으면 소수
               
                
               
       

def main():
    sosoo()

main()


