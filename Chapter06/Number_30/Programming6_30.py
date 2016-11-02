import GYKHead

		
def main():
	loseflag = 0
	winflag = 0
	for i in range(0,10000) : # 게임 run
		flag = GYKHead.playCraps()
		if flag == 0 :
			#print("You Lose!")
			loseflag = loseflag + 1
		else :
			#print("You Win!")
			winflag = winflag + 1
	print("Win times : ", winflag)
	print("Win rate : " , winflag / 100, "%")

main()