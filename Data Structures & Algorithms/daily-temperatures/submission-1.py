class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)<1:
            return []
        result=[0]* len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            if not stack or stack[-1][0] >= t:
                stack.append([t,i])
            else :
                while stack and stack[-1][0] < t:
                    curr=stack.pop()
                    result[curr[1]]=i-curr[1]
                stack.append([t,i])
        return result

