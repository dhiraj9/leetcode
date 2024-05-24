class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = 0
        b = nums[0]
        for i in nums:
            if a < 0:
                a = 0
            a += i
            b = max(a, b)
        return b
