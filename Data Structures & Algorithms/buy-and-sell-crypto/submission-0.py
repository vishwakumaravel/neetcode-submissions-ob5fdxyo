class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    if (prices[j] - prices[i]) > maxDiff:
                        maxDiff = prices[j] - prices[i]
        return maxDiff
        