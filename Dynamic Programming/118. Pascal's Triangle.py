# Easy
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for _ in range(numRows - 1):
            newRow = [1]
            for i in range(1, len(out[-1])):
                newRow.append(out[-1][i - 1] + out[-1][i])
            newRow.append(1)
            out.append(newRow)
        return out
