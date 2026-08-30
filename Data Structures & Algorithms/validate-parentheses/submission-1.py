class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='[' or ch== '{' or ch=='(':
                stack.append(ch)
            else:
                curr=stack.pop()
                if ch=='[' and curr!=']':
                    return False
                if ch=='(' and curr!=')':
                    return False
                if ch=='{' and curr!='}':
                    return False             
        return True       