class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i],speed[i]])
        pairs.sort()
        for p in pairs[-1::-1]:
            distanceLeft = target - p[0]
            if distanceLeft / p[1] > distanceLeft // p[1]:
                timeRemaining = distanceLeft // p[1] + 1
            else :
                timeRemaining = distanceLeft // p[1]
            if not stack or stack[-1] < timeRemaining:
                stack.append(timeRemaining)

        return len(stack)