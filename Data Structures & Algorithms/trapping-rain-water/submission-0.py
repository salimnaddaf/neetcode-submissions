class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) -1
        maxLeft = height[left]
        maxRight = height[right]
        result = 0

        while left <= right:
            if maxLeft <= maxRight:
                if height[left] < maxLeft:
                    result += maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                if height[right] < maxRight:
                    result += maxRight - height[right]
                maxRight = max(maxRight , height[right])
                right -= 1
        return result