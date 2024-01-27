# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        r = []
        while q:
            l = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    l.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if l:
                r.append(l[-1])
        return r


