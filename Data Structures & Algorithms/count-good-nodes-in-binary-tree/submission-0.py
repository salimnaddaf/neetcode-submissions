# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        goods = [0]
        def findGoods(root):
            if not stack or root.val >= stack[-1]:
                goods[0]+=1
                stack.append(root.val)
            if root.left:
                findGoods(root.left)
            if root.right:
                findGoods(root.right)
            if root.val == stack[-1]:
                stack.pop()
        findGoods(root)
        return goods[0]

