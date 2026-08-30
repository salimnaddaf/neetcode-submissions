class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftInd = 0
        rightInd = len(heights) -1
        maxi = 0
        while rightInd>leftInd:
            left=heights[leftInd]
            right=heights[rightInd]
            maxi=max(min(left,right)*(rightInd-leftInd),maxi)
            if right>left:
                leftInd += 1
            else: 
                rightInd -= 1
        return maxi