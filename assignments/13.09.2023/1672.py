class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        temp = 0
        for i in range(0,len(accounts)):
            for j in range(0,len(accounts[i])):
                sum = sum + accounts[i][j]
                if temp<sum:
                    temp = sum
            sum = 0
        return temp