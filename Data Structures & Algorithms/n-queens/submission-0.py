class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cBoard = [["."] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in cBoard]
                res.append(copy) 
                return
            for c in range(n):
                if self.isSafe(r, c, cBoard):
                    cBoard[r][c] = "Q"
                    backtrack(r+1)
                    cBoard[r][c] = "."

        backtrack(0)
        return res

    def isSafe(self, r: int, c: int, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True