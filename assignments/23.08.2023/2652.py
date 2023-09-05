<<<<<<< HEAD
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i
=======
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i
>>>>>>> d4cd3bf758bf3a38590eca3e6178a80ea2f9272b
        return sum