# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = [True]
        def checkTrees(pN,qN):
            if pN != qN or pN.left != qN.left or pN.right != qN.right:
                result[0] = False
            checkTrees(pN.left,qN.left)
            checkTrees(pN.right,qN.right)
        checkTrees(p,q)
        return result[0]