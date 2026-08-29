class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        total=1
        for i in range(len(nums)-1):
            total*=nums[i]
            result[i+1]*=total
        total=1
        for i in range(len(nums)-1,0,-1):
            total*=nums[i]
            result[i-1]*=total
        return result
        
