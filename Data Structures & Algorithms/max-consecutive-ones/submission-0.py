class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        for x in nums:
            if x == 1:
                count += 1
                curr = max(curr, count)
            else:
                count = 0
        return curr