# Medium
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# TC: O(6 * n)
# SC: O(1)
import math
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        out = math.inf
        for i in range(1, 7):
            a, b = 0, 0
            for j in range(len(tops)):
                if tops[j] == i and bottoms[j] == i:
                    continue
                elif tops[j] == i:
                    b += 1
                elif bottoms[j] == i:
                    a += 1
                else:
                    break
            else:
                out = min(out, a, b)
        if out == math.inf:
            return -1
        return out