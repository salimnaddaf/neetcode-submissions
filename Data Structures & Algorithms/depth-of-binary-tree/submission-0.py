# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        depth = 0
        if root:
            queue.append(root)
            depth += 1
            while queue:
                currIterations = len(queue)
                for i in range(currIterations):
                    currentNode = queue.popleft()
                    left = currentNode.left
                    right = currentNode.right
                    if left:
                        queue.append(left)
                    if right:
                        queue.append(right)
                if queue:
                    depth+=1
        return depth
