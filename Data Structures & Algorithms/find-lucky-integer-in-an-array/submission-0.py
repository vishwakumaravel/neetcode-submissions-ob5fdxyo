from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        
        # 1. Count frequencies accurately
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # 2. Initialize mx to -1 (the default return value if no lucky number exists)
        mx = -1 
        
        # 3. Iterate through the unique numbers (keys) in our frequency map
        for x, count in freq.items():
            if x == count:
                mx = max(mx, x)
                
        return mx
