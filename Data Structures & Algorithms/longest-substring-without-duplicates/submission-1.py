class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsMap = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] in charsMap:
                left = max(left,charsMap[s[right]]) + 1
            charsMap[s[right]] = right 
            result = max(result, right - left +1)
        return result