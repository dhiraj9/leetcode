class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i, j in a.items():
            if j > len(nums) / 2:
                return i

