class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        exp = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != exp[i]:
                res += 1
        return res