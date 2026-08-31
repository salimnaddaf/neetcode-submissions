class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets= set()
        for i in range(len(position)):
            remainingDistance = target-position[i]
            fleetsIn = (remainingDistance + speed[i] - 1) // speed[i] 
            fleets.add( fleetsIn )
        return len(fleets)