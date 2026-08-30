class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            while i>0  and i< len(nums) and nums[i]==nums[i-1]:
                i+=1
            left=i+1
            right=len(nums)-1
            while right>left:
                number=nums[i]+nums[left]+nums[right]
                if number==0:
                    res+=[[nums[i],nums[left],nums[right]]]
                    numLeft=nums[left]
                    while numLeft==nums[left] and left<right:
                        left+=1
                    numRight=nums[right]
                    while numRight==nums[right] and right>left:
                        right-=1
                elif number<0:
                    left+=1
                else:
                    right-=1
        return res