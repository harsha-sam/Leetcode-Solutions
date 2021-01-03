# Medium
# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity : O(M * N)
        # Space Complexity : O(N) (As we are only storing prev row)
        prev = [1 for _ in range(n)]
        for row in range(1, m):
            for col in range(1, n):
                # Add everything diagonally                 
                prev[col] = prev[col] + prev[col - 1]
        return prev[-1]

    # Example m = 5 n = 4
    #   0	1	1	1
    #   1	2	3	4
    #   1	3	6	10
    #   1	4	10	20
    #   1	5	15	35
    #   1	6	21	56