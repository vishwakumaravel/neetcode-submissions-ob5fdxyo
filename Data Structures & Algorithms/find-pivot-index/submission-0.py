class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[0:i+1]) == sum(nums[i:len(nums)]):
                return i
        return -1