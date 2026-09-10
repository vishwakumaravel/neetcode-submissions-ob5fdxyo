from collections import Counter
from typing import List

class Solution:
    def checkCounts(self, str1, str2):
        # Returns True if str1 can form str2 (all chars in str2 exist in str1 with enough frequency)
        return not (Counter(str2) - Counter(str1))

    def countCharacters(self, words: List[str], chars: str) -> int:
        total_sum = 0
        for w in words:
            if self.checkCounts(chars, w):  # Added self.
                total_sum += len(w)
        return total_sum
