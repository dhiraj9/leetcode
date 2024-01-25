class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        b = math.ceil(len(nums) / 2)
        for i, j in a.items():
            if j >= b:
                return i
