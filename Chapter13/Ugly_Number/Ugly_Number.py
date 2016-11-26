class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        num = (int)(num)
        if num == 1: # 1, 0은 예외 처리
            return True
        elif num == 0: # 1, 0은 예외 처리
            return False
        while num % 2 == 0: 
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        #Ugly Number의 조건으로 검사.
        if num == 1: # 2,3,5만으로 나누어 떨어지면 1이 되어야 함.
            return True
        else : # 아닌 경우
            return False