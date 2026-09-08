# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = [True]
        def checValid(node):
            left = node.left
            right = node.right

            if left and left.val >= root.val:
                result[0]=False
            if right and right.val <= root.val:
                result[0]=False
            if left:
                checValid(left)
            if right:
                checValid(right)
        checValid(node)
        return result[0]

        