class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        r=[-1]*len(nums)
        for i in list(range(len(nums)))*2:
            while stack and (nums[stack[-1]]<nums[i]):
                r[stack.pop()] = nums[i]
            stack.append(i)
        return r