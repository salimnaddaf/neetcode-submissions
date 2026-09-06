class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def calcRob(nums) -> int:
            rob1 = 0
            rob2 = 0
            for num in nums:
                temp = max(num+rob1,rob2)
                rob1=rob2
                rob2=temp
            return max(rob1,rob2)
        return max(calcRob(nums[0:-1]),calcRob(nums[1:len(nums)]))
