class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []       
        def traverse(candid, arr,sum):                  
            if sum == target: ans.append(arr)       
            if sum >= target: return                    
            for i in range(len(candid)):                
                traverse(candid[i:], arr + [candid[i]], sum+candid[i])
                 
        traverse(candidates,[], 0)
        return ans