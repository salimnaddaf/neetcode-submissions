class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i],speed[i]])
        pairs.sort()
        for p in pairs[-1::-1]:
            distanceLeft = target - p[0]
            timeRemaining = (distanceLeft + 1) //p[1]
            if not stack or stack[-1] < timeRemaining:
                stack.append(timeRemaining)

        return len(stack)