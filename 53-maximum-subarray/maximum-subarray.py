class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, m = 0, float('-inf')
        for i in nums:
            s += i
            m = max(s, m)
            if s < 0:
                s = 0
        return m

