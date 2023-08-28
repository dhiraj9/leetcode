class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        minimum = float('inf')
        while l <= h:
            mid = (l + h) // 2
            if nums[l] <= nums[h]:
                minimum = min(minimum, nums[l])
                break
            if nums[mid] >= nums[l]:
                minimum = min(minimum, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[h]:
                minimum = min(minimum, nums[mid])
                h = mid - 1
        return minimum