class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0
        left = 0
        first = 0 
        maxi = 1
        counter = k
        cur = s[0]
        for i in range(1,len(s)):
            if s[i] == cur:
                maxi=max(maxi,i-first+1)
            else:
                left = i
                counter-=1
                if counter < 0:
                    first = left
                    counter = k
        return maxi

                
            