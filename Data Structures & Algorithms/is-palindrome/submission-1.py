class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=''
        for ch in s:
            st+=(ch if ch.isalnum() else '')
        left=0
        right=len(st)-1
        while right>left:
            if st[left]!=st[right]:
                return False
            left+=1
            right-=1
        return True