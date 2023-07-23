class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    rows, cols = dr + r, dc + c
                    if rows < 0 or rows == ROWS or cols < 0 or cols == COLS or grid[rows][cols] != 1:
                        continue
                    queue.append([rows, cols])
                    grid[rows][cols] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
