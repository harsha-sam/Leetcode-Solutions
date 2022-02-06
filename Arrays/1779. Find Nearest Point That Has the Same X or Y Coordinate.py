# Easy
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
# Tc: O(N)

from math import inf


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def findManhattanDist(pt1, pt2):
            x1, y1 = pt1
            x2, y2 = pt2
            return abs(x1 - x2) + abs(y1 - y2)

        minD = inf
        ind = -1
        for index, pt in enumerate(points):
            if x == pt[0] or y == pt[1]:
                md = findManhattanDist((x, y), pt)
                if md < minD:
                    minD = md
                    ind = index
        return ind
