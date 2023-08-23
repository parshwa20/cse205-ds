class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def pow(n):
            if n==1:
                return True
            if n==0 or n%2!=0:
                return False
            return pow(n/2)
        return pow(n)