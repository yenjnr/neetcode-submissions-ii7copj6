class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        indegree = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for i in range(m):
            for j in range(n):
                for x, y in dirs:
                    cr, cc = i + x, j + y
                    if 0 <= cr < m and 0 <= cc < n and matrix[cr][cc] < matrix[i][j]:
                        indegree[i][j] += 1
                if indegree[i][j] == 0:
                    q.append((i, j))
        ans = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for x, y in dirs:
                    cr, cc = r + x, c + y
                    if 0 <= cr < m and 0 <= cc < n and matrix[cr][cc] > matrix[r][c]:
                        indegree[cr][cc] -= 1
                        if indegree[cr][cc] == 0:
                            q.append((cr, cc))
            ans += 1
        return ans               
