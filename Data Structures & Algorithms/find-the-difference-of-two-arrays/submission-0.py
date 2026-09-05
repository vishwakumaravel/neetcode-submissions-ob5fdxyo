class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use set difference (-) to find unique elements
        arr1 = list(set1 - set2)
        arr2 = list(set2 - set1)
        
        return [arr1, arr2]
