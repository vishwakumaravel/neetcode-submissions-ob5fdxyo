from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        nums = [str(num) for num in nums]
        
        # Custom comparator: return -1 if n1+n2 should come first, 1 if n2+n1 should, 0 if equal
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            return 0
        
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join and handle edge cases like ["0", "0"] -> "0"
        return str(int("".join(nums)))
