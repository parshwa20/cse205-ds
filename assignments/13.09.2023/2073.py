class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        if tickets[k] == 0:
            return 0
        
        i = 0
        ans = 0

        while True:
            if tickets[i]:
                tickets[i] -= 1
                ans += 1

            if i == k and tickets[i] == 0:
                return ans
            
            i += 1