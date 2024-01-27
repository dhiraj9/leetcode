import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        queue = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1
