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
            #left sorted
            if mid > left:
                if mid > target >= left:
                    rightI = midI - 1
                else:
                    leftI = midI + 1
            else:
            #right sorted
                if right >= target > mid :
                    leftI = midI + 1
                else :
                    rightI = midI - 1
                     
        return -1