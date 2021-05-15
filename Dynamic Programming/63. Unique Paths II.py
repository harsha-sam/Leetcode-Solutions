# Medium
# https://leetcode.com/problems/unique-paths-ii/ 

# TC: O(M * N)
# SC: O(N)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        prev_row = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        prev_row[j] = 1
                    elif j > 0:
                        prev_row[j] += prev_row[j - 1]
                else:
                    prev_row[j] = 0
        return prev_row[-1]