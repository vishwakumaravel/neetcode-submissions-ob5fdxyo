class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            sum = max(sum, len(charSet))
        return sum