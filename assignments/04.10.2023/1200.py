class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid =len(arr)//2
            left,right=arr[:mid],arr[mid:]
            left,right = merge_sort(left),merge_sort(right)
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
        arr = merge_sort(arr)
        x = 100000
        for i in range(len(arr)-1):
            z = arr[i+1] - arr[i]
            if z<x:
                x = z
        final =[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == x:
                final.append([arr[i], arr[i+1]])
        return final