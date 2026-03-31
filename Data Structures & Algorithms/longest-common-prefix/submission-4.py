class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        testin = []
        newStr = ""
        for i in range(len(strs[0])):
            for x in strs:
                if i < len(x):
                    testin.append(x[i])
                else:
                    return newStr
            if len(set(testin)) != 1:
                if i == 0:
                    return ""
                else:
                    return newStr
            newStr += strs[0][i]
            testin = []
        return newStr 


            
