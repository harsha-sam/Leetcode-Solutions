# https://leetcode.com/problems/word-search/
# TC: O(4 * m * n)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recur_solve(x, y, i):
            if (not 0 <= x < len(board)) or (not 0 <= y < len(board[0])) or vis[x][y] or word[i] != board[x][y]:
                return False
            vis[x][y] = True
            if i == len(word) - 1 and board[x][y] == word[-1]:
                return True
            if recur_solve(x, y + 1, i + 1) or recur_solve(x, y - 1, i + 1) or recur_solve(x + 1, y, i + 1) or recur_solve(x - 1, y, i + 1):
                return True
            vis[x][y] = False

        vis = [[False for _ in range(len(board[0]))]for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and recur_solve(i, j, 0):
                    return True
