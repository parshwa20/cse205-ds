class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left,right=arr[:mid],arr[mid:]
            left,right=merge_sort(left),merge_sort(right)
            result,i,j=[],0,0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        a=merge_sort(prices)
        for i in range(len(a)):
            if a[i]+a[i+1]<=money:
                return money - (a[i]+a[i+1])
            else:
                return money