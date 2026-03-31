class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newNums = []
        for i in range(len(nums)):
            if nums[i] != val:
                newNums.append(nums[i])
        for i in range(len(newNums)):
            nums[i] = newNums[i]
        return len(newNums)
        
                