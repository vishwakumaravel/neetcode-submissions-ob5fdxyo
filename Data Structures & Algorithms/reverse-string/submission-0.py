class Solution:
    def reverseString(self, s: List[str]) -> None:
        sN = []
        for i in range(len(s)-1, -1, -1):
            if i >= 0:
                sN.append(s[i])
        s[:] = sN
        return s


        