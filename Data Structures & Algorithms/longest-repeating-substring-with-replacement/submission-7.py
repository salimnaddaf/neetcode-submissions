class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        charsMap = {}
        for right in range(len(s)):
            charsMap[s[right]] = charsMap.get(s[right],0)+1
            while right - left + 1 > max(charsMap.values()) + k:
                charsMap[s[left]] -= 1
                left +=1
            result = max(result,right-left+1)

        return result
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

                
            