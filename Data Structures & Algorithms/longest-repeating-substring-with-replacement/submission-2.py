class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        maxi = 0
        left = 0

        for right  in range(len(s)):
            chars [s[right]] = chars.get(s[right],0)+1
            while right - left + 1 - max(chars.values()) > k:
                chars [s[left]] -= 1
                left+=1
            maxi=max(maxi,right-left+1)

        return maxi

                
            