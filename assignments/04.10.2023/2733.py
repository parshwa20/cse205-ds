class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=2:
            return -1
        else:
            if nums[1]<nums[-1] and nums[1]>nums[0]:
                return nums[1]