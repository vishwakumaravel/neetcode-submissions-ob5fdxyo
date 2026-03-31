class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums.sort()
            if nums[i] == nums[len(nums)//2]:
                return nums[i]
            




        # greatest = 0
        # topNum = 0
        # for i in range(len(nums)):
        #     if nums.count(nums[i]) > greatest:
        #         greatest = nums.count(nums[i])
        #         topNum = nums[i]
        # return topNum