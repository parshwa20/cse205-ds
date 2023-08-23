class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a=0
        for i in range(0,len(nums)):
            if len(str(nums[i]))%2==0:
                a=a+1
        return a