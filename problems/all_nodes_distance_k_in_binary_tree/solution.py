# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                queue.append(node.left)
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                queue.append(node.right)
        queue = collections.deque([(target, 0)])
        visited = set([target])
        result = []
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                result.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, distance + 1))
        return result
