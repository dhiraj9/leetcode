class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
#         if len(nums)%2==0:
#             m = (nums[len(nums/2)]+nums[len(nums/2)-1])/2
#         else:
#             m = nums[(len(nums)+1)/2]
#         if target>nums[m]:
#             l=m+1
#         elif target<nums[m]:
#             h=m-1
#         else:
#             return m
#         if i not 
        
            
        
        