class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars=[0]*26
        for sCh in s:
            chars[ord(sCh)-ord('a')]+=1
        for tCh in t:
            chars[ord(tCh)-ord('a')]-=1
        for ch in chars:
            if ch!=0:
                return False
        return True
