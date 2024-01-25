# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        c = -1
        while q:
            c = c + 1
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
        return c

