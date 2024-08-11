class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        result = 0
        while L < R:
            result = max(result, min(height[L], height[R]) * (R - L))
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return result
        