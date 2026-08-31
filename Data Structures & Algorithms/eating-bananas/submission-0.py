class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        mini = max(piles)
        while right >= left:
            mid = (right + left) // 2
            curr=0
            for num in piles:
                if mid >= num:
                    curr+=1
                else:
                    curr+= (num + mid -1) //mid
            if curr> h:
                left = mid + 1
            else:
                right = mid -1
                mini = min(mini,mid)
        return mini
