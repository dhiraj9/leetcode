class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            ans = max(sum, ans)
        return ans



