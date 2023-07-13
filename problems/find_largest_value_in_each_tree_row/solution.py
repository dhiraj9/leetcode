# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            max_seen = float('-inf')
            for i in range(len(q)):
                node = q.popleft()
                max_seen = max(max_seen, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(max_seen)
        return result