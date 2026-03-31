class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs_sub = []
        strs_main = []
        for i in range(len(strs)):
            if i >= len(strs):
                break
            strs_sub = []
            strs_sub.append(strs[i])
            for j in range(len(strs)-1, i, -1):
                if i != j:
                    if sorted(strs[i]) == sorted(strs[j]):
                        strs_sub.append(strs.pop(j))
            strs_main.append(strs_sub)
        return strs_main