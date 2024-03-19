class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = set()
        for i, j in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                b = nums[l] + nums[r] + j
                if b == 0 and (j, nums[l], nums[r]) not in a:
                    a.add((j, nums[l], nums[r]))
                elif b > 0:
                    r -= 1
                else:
                    l += 1
        return list(a)


            




