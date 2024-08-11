class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i, j in enumerate(nums):
            if i > 0 and j == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                temp = nums[L] + nums[R] + j
                if temp == 0:
                    result.append([nums[L], nums[R], j])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif temp > 0:
                    R -= 1
                else:
                    L += 1
        return result

        