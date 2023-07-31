class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            tmp = []
            for leaf in leaves:
                for i in neighbors[leaf]:
                    neighbors[i].remove(leaf)
                    if len(neighbors[i]) == 1:
                        tmp.append(i)
            leaves = tmp
        return leaves
