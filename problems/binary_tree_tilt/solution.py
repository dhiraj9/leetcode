# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        def findSum(node):
            if not node:
                return 0
            l = findSum(node.left)
            r = findSum(node.right)
            self.tilt += abs(l - r)
            return l + r + node.val
        findSum(root)
        return self.tilt