# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1, 0]])
        result = 0
        prevNum, prevLvl = 1, 0
        while q:
            node, num, level = q.popleft()
            if level > prevLvl:
                prevLvl = level
                prevNum = num
            result = max(result, num - prevNum + 1)
            if node.left:
                q.append([node.left, 2 * num, prevLvl + 1])
            if node.right:
                q.append([node.right, 2 * num + 1, prevLvl + 1])
        return result