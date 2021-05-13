# Easy
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# TC:O(N)
# SC:O(1)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, out = 0, 0
        for letter in s:
            if letter == 'L':
                count += 1
            elif letter == 'R':
                count -= 1
            if count == 0:
                out += 1
        return out