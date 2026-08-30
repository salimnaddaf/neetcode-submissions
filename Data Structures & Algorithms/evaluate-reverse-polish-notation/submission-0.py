class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        stack = []
        for s in tokens:
            if s.isnumeric():
                stack.append(int(s))
            else:
                a=stack.pop()
                b=stack.pop()
                if s=='+':
                    stack.append(a+b)
                if s=='-':
                    stack.append(a-b)
                if s=='*':
                    stack.append(a*b)
                if s=='/':
                    stack.append(a/b)                                                        
        return stack.pop()