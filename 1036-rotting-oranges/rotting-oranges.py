class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh = fresh + 1
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append([r, c])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1



