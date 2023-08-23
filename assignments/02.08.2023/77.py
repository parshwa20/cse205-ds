class Solution:
    def comb(self,lst,k,ans,temp,index):
        if len(temp) == k:
            ans.append(temp.copy())
            return
        for i in range(index,len(lst)):
            temp.append(lst[i])
            self.comb(lst,k,ans,temp,i+1)
            temp.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        lst = [i for i in range(1,n+1)]
        self.comb(lst,k,ans,[],0)
        return ans
