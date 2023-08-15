# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        def dfs(node, path, sm):
            sm += node.val
            tmp = path + [node.val]
            if node.left:
                dfs(node.left, tmp, sm)
            if node.right:
                dfs(node.right, tmp, sm)
            if not node.right and not node.left and sm == targetSum:
                self.output.append(tmp)
        if not root:
            return []
        dfs(root, [], 0)
        return self.output