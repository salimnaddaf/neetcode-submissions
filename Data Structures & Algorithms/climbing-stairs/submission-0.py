class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def calculate(n,memo) -> int:
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n < 1:
                return 0
            if n == 2:
                return 2
            curr = calculate(n-1,memo) + calculate(n-2 , memo)
            memo[n] = curr
            return curr
        return calculate(n,memo)