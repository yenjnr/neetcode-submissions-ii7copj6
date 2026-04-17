class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs from all starting positions
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n = len(matrix)
        m = len(matrix[0])

        # can we use a different algorithm than dfs to do this?
        # the max path can be found by the number of iterations of topo sort i think
        indegree = [0] * (m * n)
        for i in range(n):
            for j in range(m):
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < m and matrix[i][j] > matrix[nr][nc]:
                        indegree[(i * m) + j] += 1


        # for i in range(n):
        #     for j in range(m):
        #         print(indegree[(i * m) + j], end=', ')
        #     print()
        
        # print('_' * 10)

        steps = 0
        q = deque([i for i in range(m * n) if indegree[i] == 0])
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                i, j = x // m, x % m
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < m and matrix[i][j] < matrix[nr][nc]:
                        indegree[(nr * m) + nc] -= 1
                        if indegree[(nr * m) + nc] == 0:
                            q.append((nr * m) + nc)
            steps += 1

        # for i in range(n):
        #     for j in range(m):
        #         print(indegree[(i * m) + j], end=', ')
        #     print()

        return steps

        # 2D coordinate array, where the value at each is a map that maps the current val to the number of paths
        # dp = [[-1] * (m + 1) for _ in range(n + 1)]

        # def dfs(i, j):
        #     if dp[i][j] == -1:
        #         for dr, dc in directions:
        #             nr, nc = i + dr, j + dc
        #             if 0 <= nr < n and 0 <= nc < m and matrix[i][j] < matrix[nr][nc]:
        #                 dp[i][j] = max(dp[i][j], dfs(nr, nc) + 1)

        #         dp[i][j] = max(dp[i][j], 0) # could be no valid paths out, so update it from -1

        #     return dp[i][j]

        # res = 0
        # for i in range(n):
        #     for j in range(m):
        #         res = max(res, dfs(i, j) + 1)

        # return res