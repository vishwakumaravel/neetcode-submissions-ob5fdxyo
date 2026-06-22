from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        duplicate = -1
        missing = -1
        
        # Numbers are strictly in the range [1, n]
        for i in range(1, n + 1):
            if counts[i] == 2:
                duplicate = i
            elif counts[i] == 0:
                missing = i
                
        return [duplicate, missing]
