class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        temp = 0
        current = 1
        last = 0
        if n == 1 : # 첫 번째 값은 0 (0 , 1 , 1 , 2 , 3 , 5 - - - )
            return 0
        for i in range(2, n): 
            temp = current # 현재 값을 임시변수에 저장
            current += last # 현재 값에 이전 값을 더함
            last = temp # 이전 값은 바로 직전의 현재 값으로 바꾸어 줌
        return current
