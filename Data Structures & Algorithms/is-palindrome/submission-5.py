class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ch in s:
            if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
                ch=chr(ord(ch)+32)
            if( ord(ch)>=ord('a') and ord(ch)<=ord('z') or ord(ch)>=ord('0') and ord(ch)<=ord('9')):
                st+=ch
        left=0
        right=len(st)-1
        return st[::1]==st[::-1]