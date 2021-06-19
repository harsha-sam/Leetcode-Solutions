# DFS
# Medium
# https://leetcode.com/problems/number-of-islands/

# TC: O(n)
# SCL O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if (not 0 <= x < len(grid)) or (not 0 <= y < len(grid[0])) or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    out += 1
        return out
