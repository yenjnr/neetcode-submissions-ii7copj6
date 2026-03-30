class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        
        for i in prices:
            profit = max(profit, i - lowest)
            lowest = min(lowest, i)
        return profit