class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while right > left:
            curr=numbers[left]+numbers[right]
            if curr==target:
                return [numbers[left],numbers[right]]
            if curr > target:
                right-=1
            else:
                left+=1
        return []