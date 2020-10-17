# Medium
# https://leetcode.com/problems/spiral-matrix/
# Time Complexity: O(N)
# Space Complexity: 0(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return Solution.spiralsol(matrix, [])
    
    @staticmethod
    def spiralsol(matrix, res):
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        if n == 0:
            return res
        res += matrix[0]
        if m > 1:
            res += [matrix[i][n - 1] for i in range(1, m - 1)]
            res += matrix[m - 1][::-1]
            if n > 1:
                res += [matrix[i][0] for i in range(m - 2, 0, -1)]
            matrix = matrix[1:m - 1]
            for index, row in enumerate(matrix):
                matrix[index] = row[1:n-1]
            Solution.spiralsol(matrix, res)
        return res