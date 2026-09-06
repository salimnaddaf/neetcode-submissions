class Solution:
    def longestPalindrome(self, s: str) -> str:

        def calcPali(left,right) -> str:
            res = s[left:right]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = s[left:right+1]
                left -=1
                right +=1
            return res
                    
        if len(s) == 0:
            return 0
        result = ""
        for i in range(len(s)):
            odd = calcPali(i,i)
            if len(odd) > len(result):
                result = odd
            even = calcPali(i,i+1)
            if len(even) > len(result):
                result = even
        return result


          