# Medium
# https://leetcode.com/problems/rotate-image/

# TC: O(N * N)
# SC: O(1)

# Solution: Tranform the matrix and reverse
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
