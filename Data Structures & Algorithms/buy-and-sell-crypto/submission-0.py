class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 1:
            return 0
        min = prices[0]
        for num in prices[1::]:
            if num < min:
                min = num
            if num > min:
                profit = max(profit,num-min)
        return profit