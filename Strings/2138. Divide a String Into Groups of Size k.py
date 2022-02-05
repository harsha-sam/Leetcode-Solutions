# TC, SC: O(N)
# Easy
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        rem = len(s) % k
        out = []
        for i in range(0, len(s), k):
            out.append(s[i:i+k])
        if rem:
            out[-1] += (k - rem) * fill
        return out
