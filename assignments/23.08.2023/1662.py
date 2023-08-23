class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1=""
        v2=""
        for i in range(len(word1)):
            v1=str(v1)+str(word1[i])
        for j in range(len(word2)):
            v2=str(v2)+str(word2[j]) 

        return v1==v2