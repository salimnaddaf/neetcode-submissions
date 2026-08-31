class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftI = 0
        rightI = len(nums)-1
        while leftI <= rightI:
            left = nums[leftI]
            right = nums[rightI]
            if left == right:
                return left
            midI = (leftI + rightI) //2
            mid = nums[midI]
            if left > right:
                if left <= mid:
                    leftI = midI + 1
                else:
                    rightI = midI
            if left < right:
                return left
        return 0
        # 7 8 9 10 11 12 13 1 2 3 4 5 6 