class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if a + nums[r] + nums[l] == 0:
                    result.append([a, nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif a + nums[r] + nums[l] > 0:
                    r -= 1
                else:
                    l += 1
        return result


