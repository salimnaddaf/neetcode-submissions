class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s.isnumeric():
                stack.append(int(s))
            else:
                b=stack.pop()
                a=stack.pop()
                if s=='+':
                    stack.append(a+b)
                elif s=='-':
                    stack.append(a-b)
                elif s=='*':
                    stack.append(a*b)
                elif s=='/':
                    stack.append(int(a/b))                                                        
        return int(stack.pop())