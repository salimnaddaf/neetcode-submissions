class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftI = 0 
        rightI = len(nums) -1

        while leftI <= rightI:
            #declare Mid
            midI = (leftI + rightI) //2
            #attributes left , right , mid
            left = nums[leftI]
            right = nums[rightI]
            mid = nums[midI]
            #we got the nuber
            if mid==target:
                return midI
            #we didn't get the number
            if left > right:
                if left <= target:
                    rightI = midI - 1
                else:
                    leftI = midI + 1
            else:
                if mid > target:
                    rightI= midI - 1
                else :
                    leftI = midI + 1
        return -1