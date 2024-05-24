class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        a = [0]
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            b = 1 + max(left, right)
            a[0] = max(a[0], b)
            return b
        dfs(root)
        return a[0]
