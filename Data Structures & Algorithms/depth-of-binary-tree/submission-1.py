# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        maxi = 0
        if root:
            stack.append([root,1])
            while stack:
                curr = stack.pop()
                if curr[0].right:
                    stack.append([curr[0].right,curr[1]+1])
                if curr[0].left:
                    stack.append([curr[0].left,curr[1]+1])
                maxi = max(maxi,curr[1])
        return maxi