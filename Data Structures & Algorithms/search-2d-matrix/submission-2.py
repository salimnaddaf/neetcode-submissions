class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target and row[0] <= target:
                return self.binarySearch(row,target)
        return True
                
    
    def binarySearch(self, arr: List[int], target: int) ->bool:
        left = 0
        right = len(arr) -1
        while left <= right:
            mid = (right-left) + left //2
            curr = arr[mid]
            if curr==target:
                return True
            if curr > target:
                right = mid-1
            else:
                left = mid+1
        return False