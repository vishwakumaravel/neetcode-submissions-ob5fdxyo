from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        freq = Counter(s)
        for char in s:
            if freq[char] == 1:
                return i
            i = i+1
        return -1