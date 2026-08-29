class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        counter=0
        maxi=0
        for num in numSet:
            if num+1 in numSet:
                counter=1
                while num+1 in numSet:
                    counter+=1
                    num+=1
                maxi=max(counter,maxi)
                counter=0
        return maxi