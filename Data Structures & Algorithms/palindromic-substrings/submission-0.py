class Solution:
    def countSubstrings(self, s: str) -> int:
        def calcPali(left,right) -> int:
            counter = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter+=1
                left-=1
                right+=1
            return counter

        
        result = 0
        for i in range(len(s)):
            result+=calcPali(i,i) + calcPali(i,i+1)
        return result