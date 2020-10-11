# Hard
# https://leetcode.com/problems/edit-distance/submissions/
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        d[i][j] = d[i-1][j-1]
                    else:
                        d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1
        return d[n][m]