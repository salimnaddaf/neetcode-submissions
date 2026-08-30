class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)<1:
            return []
        result=[0]* len(temperatures)
        maxi = temperatures[len(temperatures)-1]
        maxiInd = len(temperatures)-1
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] < temperatures[i+1]:
                result[i]=1
            else:
                if temperatures[i] >= maxi:
                    maxi = temperatures[i]
                    maxiInd = i
                else:
                    result[i] = maxiInd - i
                    
        return result

