class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si = list(s)
        ti = list(t)

        if len(si) != len(ti):
            return False
        for i in range(len(si)):
            for j in range(len(ti)):
                if si[i] == ti[j]:
                    ti.pop(j)
                    break
        if len(ti) == 0:
            return True
        else:
            return False