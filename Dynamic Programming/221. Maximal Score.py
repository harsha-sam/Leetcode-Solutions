# Medium
# Refer https://www.byte-by-byte.com/squaresubmatrix/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
# https://leetcode.com/problems/maximal-square/
class Solution:
# Time Complexity: O(m * n)    
# Space Complexity: O(m * n)
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     m = len(matrix)
    #     if m == 0:
    #         return 0
    #     n = len(matrix[0])
    #     if n == 0:
    #         return 0
    #     d = [[0 for _ in range(n)]for _ in range(m)]
    #     maxi = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 or j == 0:
    #                 d[i][j] = int(matrix[i][j])
    #             elif matrix[i][j] == "1":
    #                 d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1
    #             maxi = max(d[i][j], maxi)
    #     return maxi * maxi

# Another solution is to just store the i - 1th row because we are only comparing dp[i - 1][j] and dp[i - 1][j - 1] and dp[i][j - 1]
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Time Complexity: O(m * n)    
        # Space Complexity: O(n)
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        maxi = 0
        for i in range(m):
            temp = dp.copy()
            for j in range(n):
                if i == 0 or j == 0:
                    dp[j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp[j] = min(dp[j-1], temp[j], temp[j-1]) + 1
                else:
                    dp[j] = 0
                maxi = max(dp[j], maxi)
        return maxi * maxi