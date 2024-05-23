class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        b = floor(len(nums) / 2)
        for i, j in a.items():
            if j > b:
                return i
