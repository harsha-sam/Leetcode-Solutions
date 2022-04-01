# Medium
# https://leetcode.com/problems/diagonal-traverse/
# TC: O(N * M)
# SC: O(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        i, j = 0, 0
        flag = True
        res = []
        while i < n and j < m:
            res.append(mat[i][j])
            new_i, new_j = i, j
            new_i += -1 if flag else 1
            new_j += 1 if flag else -1
            if not (0 <= new_i < n) or not (0 <= new_j < m):
                if flag:
                    i += j == m - 1
                    j += j < m - 1
                else:
                    j += i == n - 1
                    i += i < n - 1
                flag = not flag
            else:
                i, j = new_i, new_j
        return res
            