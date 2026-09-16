class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        counter = 0
        maxi = 0
        for num in numsSet:
            if num-1 not in numsSet:
                counter = 1
                while num+1 in numsSet:
                    counter += 1
                    num += 1
            maxi = max(maxi,counter)
            
        return maxi