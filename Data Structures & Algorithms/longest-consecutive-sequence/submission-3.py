class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        numMap={}
        numSet=set()
        
        for num in nums:
            numSet.add(num)
        mini=min(numSet)
        maxi=max(numSet)
        while mini<maxi:
            if mini in numSet:
                if mini+1 in numSet:
                    numMap[mini+1]=numMap.get(mini,1)+1
            mini+=1
        if len(numMap)>0:
            return max(numMap.values())
        return 1