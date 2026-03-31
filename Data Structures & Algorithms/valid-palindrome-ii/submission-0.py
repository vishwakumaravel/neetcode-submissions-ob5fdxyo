class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                s2 = s[:i] + s[i:].replace(s[i], '', 1)
                if s2 == s2[::-1]:
                    return True
                else:
                    s2 = s
        return False