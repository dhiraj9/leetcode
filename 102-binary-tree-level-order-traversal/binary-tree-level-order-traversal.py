# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        r = []
        while q:
            a = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    a.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if a:
                r.append(a)
        return r
