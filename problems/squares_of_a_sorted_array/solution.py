class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []
        while l <= r:
            if nums[l] * nums[l] < nums[r] * nums[r]:
                result.append(nums[r] * nums[r])
                r -= 1
            else:
                result.append(nums[l] * nums[l])
                l += 1
        return result[::-1]
            