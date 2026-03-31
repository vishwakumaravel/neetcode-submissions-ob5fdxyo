class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        newStr = ""
        for i in range(max(n,m)):
            if i < n:
                newStr += word1[i]
            if i < m:
                newStr += word2[i]
        return newStr

