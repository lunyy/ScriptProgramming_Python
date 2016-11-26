class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        n = (int)(n)
        if n == 1:
            return True
        elif n == 0:
            return False
        cache = [] # 계산 결과를 저장해서 반복되는가를 검사함.
        while True:
            number = (str)(n) # 자릿수를 자르기 위해 문자열로 타입캐스팅
            n = 0
            for i in range(0,len(number)): # 각 자릿수를 제곱해서 더하기.
                n = n + (int)(number[i])**2 
            for j in range(0,len(cache)): # 이미 나온 숫자이면 False 리턴
                if n == cache[j]:
                    return False
            if n == 1: # 1이 되면 True 리턴
                return True
            cache.append(n) # n을 계산 결과 리스트에 추가.