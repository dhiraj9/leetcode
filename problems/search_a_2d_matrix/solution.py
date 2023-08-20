class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False
        l, r = 0, COLS - 1
        row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False