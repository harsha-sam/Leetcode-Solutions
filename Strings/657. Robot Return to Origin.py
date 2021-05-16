# Easy
# https://leetcode.com/problems/robot-return-to-origin/
# TC : O(N)
# SC : O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r, c = 0, 0
        for mv in moves:
            if mv == 'L':
                c -= 1
            elif mv == 'R':
                c += 1
            elif mv == 'U':
                r -= 1
            elif mv == 'D':
                r += 1
        return r == c == 0