# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def calcDia(root) ->int:
            dfsLeft = 0
            dfsRight = 0
            if root.left:
                dfsLeft = 1 + calcDia(root.left)
            if root.right:
                dfsRight = 1 + calcDia(root.right)

            maxi[0] = max(dfsRight+dfsLeft, maxi[0])
            return max(dfsRight,dfsLeft)

        calcDia(root)
        return maxi[0]

