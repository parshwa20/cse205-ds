class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def solve(p=[], nums=[]):
            if len(p) == len(nums):
                arr.append(p)
                return
            for i in range(len(nums)):
                if nums[i] not in p:
                    solve(p + [nums[i]], nums)
        solve([], nums)
        return arr