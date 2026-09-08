# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            rVal= root.val
            if  p.val == rVal or q.val == rVal or p.val> rVal > q.val or q.val > rVal > p.val:
                return root
            if rVal > p.val:
                root=root.left
            else:
                root=root.right
        return None
                
