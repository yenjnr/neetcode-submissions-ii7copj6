class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[1] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                cache[i][j] = cache[i-1][j] + cache[i][j-1]
        return cache[m-1][n-1]