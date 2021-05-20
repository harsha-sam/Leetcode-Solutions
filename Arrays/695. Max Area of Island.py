# Depth First Search
# Medium
# https://leetcode.com/problems/max-area-of-island/
# TC: O(R * C)
# SC: O(R * C)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        vis = [[False for _ in range(len(grid[0]))]for _ in range(len(grid))]
        def area(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or vis[r][c] or not grid[r][c]:
                return 0
            vis[r][c] = True
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))