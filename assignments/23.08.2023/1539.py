<<<<<<< HEAD
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[]
        b=1
        while b<=1000000:
            if b not in arr:
                a.append(b)
            if len(a)==k:
                return a[k-1]
                break
            b+=1
        
=======
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[]
        b=1
        while b<=1000000:
            if b not in arr:
                a.append(b)
            if len(a)==k:
                return a[k-1]
                break
            b+=1
        
>>>>>>> d4cd3bf758bf3a38590eca3e6178a80ea2f9272b
        