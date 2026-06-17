class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = set(nums1)
        n2 = set(nums2)

        res = []
        for x in nums1:
            if x in nums2:
                res.append(x)
        return list(set(res))
