class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    R = dr + row
                    C = dc + col
                    if (R) in range(rows) and (C) in range(cols) and (R, C) not in visited and grid[R][C] == "1":
                        visited.add((R, C))
                        queue.append((R, C))

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands