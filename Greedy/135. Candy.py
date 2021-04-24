# Hard
# https://leetcode.com/problems/candy/

# Greedy Solution : https://leetcode.com/problems/candy/solution/
# TC: O(N)
# SC: O(N)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        out = [1 for _ in range(n)]
        # Left Neighbour         
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                out[i + 1] = out[i] + 1
        s = 0
        # Right Neighbour         
        for i in range(n - 1, 0, -1):
            s += out[i]
            if ratings[i - 1] > ratings[i]:
                out[i - 1] = max(out[i] + 1, out[i-1])
        s += out[0]
        return s