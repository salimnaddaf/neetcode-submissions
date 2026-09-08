# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def calcBalance(root) ->int:
            left = 0
            right = 0
            if root.left:
                left = 1 + calcBalance(root.left)
            if root.right:
                right = 1 + calcBalance(root.right)
            if left - right > 1 or left - right < -1:
                result[0]=False
            return max(left,right)
        if not root:
            return True
        calcBalance(root)
        return result[0]