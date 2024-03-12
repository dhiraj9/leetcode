class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, j in enumerate(nums):
            b = target - nums[i]
            if b in a:
                return [i, a[b]]
            a[j] = i

