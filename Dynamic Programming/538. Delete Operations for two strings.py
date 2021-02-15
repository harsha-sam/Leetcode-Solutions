# Medium
# https://leetcode.com/problems/delete-operation-for-two-strings/
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Find the longest common substring because 
        # that would be the word we need to make such that both strings will be equal 
        n = len(word1)
        m = len(word2)
        d = [[0 for _ in range(m + 1)]for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    d[i][j] = 0
                elif word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        # the total number of characters to delete would be len(word1) - len(lcs) +             len(word2) - len(lcs)
        return n - d[n][m] + m - d[n][m]
        