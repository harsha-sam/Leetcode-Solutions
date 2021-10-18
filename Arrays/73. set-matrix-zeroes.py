# Medium
# https://leetcode.com/problems/set-matrix-zeroes/
# https://www.byte-by-byte.com/zeromatrix/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions

class Solution:  # Time Complexity : O(R * C) SPACE : O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC: O(R * C)
        # SC: O(N)
        # rows = []
        # cols = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rows.append(i)
        #             cols.append(j)
        # for r in rows:
        #     for j in range(len(matrix[0])):
        #         matrix[r][j] = 0

        # for c in cols:
        #     for i in range(len(matrix)):
        #         matrix[i][c] = 0

        # TC: O(R * C)
        # SC: O(1)
        first_row, first_col = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        first_row = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0