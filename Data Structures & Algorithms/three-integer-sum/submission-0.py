from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = set()  # holds tuples like (-1,0,1)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        trip = tuple(sorted((nums[i], nums[j], nums[k])))
                        seen.add(trip)
        return [list(t) for t in seen]
