# Easy
# https://leetcode.com/problems/jewels-and-stones/
# TC : O(J + S)
# SC : O(J)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out, d = 0, {}
        for i in jewels:
            d[i] = True
        for i in stones:
            if i in d:
                out += 1
        return out