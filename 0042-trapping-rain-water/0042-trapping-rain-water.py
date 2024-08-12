class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxLeft, maxRight = height[L], height[R]
        result = 0
        while L < R:
            if maxLeft < maxRight:
                L += 1  
                maxLeft = max(maxLeft, height[L])
                result += maxLeft - height[L]
            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                result += maxRight - height[R]
        return result

        