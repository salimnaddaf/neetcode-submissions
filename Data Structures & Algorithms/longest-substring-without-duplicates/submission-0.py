class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap={}
        left=0
        maxi=0
        for i , ch in enumerate(s):
            if ch in charMap:
                left=max(left,charMap[ch]+1)  
            charMap[ch]=i          
            maxi=max(maxi,i-left+1)
        return maxi

