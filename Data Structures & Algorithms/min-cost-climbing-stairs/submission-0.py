class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        def returnMin(i) -> int:
            if i in memo:
                return memo[i]
            if i ==1 or i == 0:
                return cost[i]
            memo[i] = cost[i] +  min(returnMin(i-1),returnMin(i-2))
            return memo[i]
        return min (returnMin(len(cost)-1),returnMin(len(cost) -2))

            
            