class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curmax, curmin = 1, 1
        for n in nums:
            if n == 0:
                curmax, curmin = 1, 1
                continue
            temp = n * curmax
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(n * curmin, temp, n)
            result = max(curmax, result)
        return result
