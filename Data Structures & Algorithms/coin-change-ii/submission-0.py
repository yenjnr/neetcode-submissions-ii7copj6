class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [0] * (amount + 1)
        cache[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                cache[a] += cache[a - coins[i]] if coins[i] <= a else 0
        return cache[amount]