import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(row, col):
            visited.add((row, col))
            queue = collections.deque()
            queue.append((row, col))
            while queue:
                r, c = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands