class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum=0
        count=0
        for num in nums:
            if num==1:
                count+=1
                maxNum=max(maxNum,count)
            else:
                count=0
        return maxNum
            