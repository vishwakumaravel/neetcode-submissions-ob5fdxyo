class Solution:
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            if n==1:
                return True
            seen.add(n)
            d=0
            c=str(n)
            for i in c:
                d+=int(i)*int(i)
            n=d
        return False
        