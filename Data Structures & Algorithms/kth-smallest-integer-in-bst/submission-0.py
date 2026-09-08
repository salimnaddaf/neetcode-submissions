# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [k]
        result = [0]
        def findSmallest(root) -> int:
            if not root:
                return

            findSmallest(root.left)
            counter[0] -= 1
            if counter[0] == 0:
                result[0] = root.val
            
            findSmallest(root.right)
        findSmallest(root)
        return result[0]
