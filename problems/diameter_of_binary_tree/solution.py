# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r = [0]
        def d(root):
            if not root:
                return -1
            left = d(root.left)
            right = d(root.right)
            r[0] = max(2 + left + right, r[0])
            return 1 + max(left, right)
        d(root)
        return r[0]
