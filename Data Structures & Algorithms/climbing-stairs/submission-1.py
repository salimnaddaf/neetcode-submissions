class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def calculate(n) -> int:
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n < 1:
                return 0
            if n == 2:
                return 2
            curr = calculate(n-1) + calculate(n-2)
            memo[n] = curr
            return curr
        return calculate(n)