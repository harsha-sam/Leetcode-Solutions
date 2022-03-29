# Easy
# https://leetcode.com/problems/first-bad-version/
# TC: O(log N)
# SC: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        pos = -1
        while l <= h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                h = mid - 1
                pos = mid
            else:
                l = mid + 1
        return pos
