class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        buy, prev_buy = -prices[0], float('-inf')
        sell, prev_sell = 0, 0
        for i in range(1, n):
            new_buy = max(buy, prev_sell - prices[i])
            new_sell = max(sell, buy + prices[i])
            prev_buy, buy = buy, new_buy
            prev_sell, sell = sell, new_sell
        return sell
