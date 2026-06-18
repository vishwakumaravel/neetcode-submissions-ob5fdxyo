class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp = {}
        for x in nums:
            mp[x] = mp.get(x,0) + 1
        for key, value in mp.items():
            if value % 2 != 0:
                return False
        return True