class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]=="*":
                if stack:
                    stack.pop()
                
            else:
                stack.append(s[i])
        a=""
        for j in range(len(stack)):
            a = a+str(stack[j])
        return a