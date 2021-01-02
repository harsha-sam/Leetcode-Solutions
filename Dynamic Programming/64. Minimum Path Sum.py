# Medium
# https://leetcode.com/problems/minimum-path-sum/
# Time Complexity : O(R * C)
# Space Complexity : O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row > 0 and col > 0:
                    grid[row][col] = grid[row][col] + min(grid[row - 1][col], grid[row][col - 1])
                elif row > 0:
                    grid[row][col] += grid[row - 1][col]
                elif col > 0:
                    grid[row][col] += grid[row][col - 1]
        return grid[-1][-1]
        