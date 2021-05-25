# Medium
# https://leetcode.com/problems/decode-ways/
# TC:O(n) as we're memoizing
# SC:O(n) 
class Solution:
    def numDecodings(self, s: str) -> int:
        def solve(s, d):
            if s in d:
                return d[s]
            elif len(s) <= 1:
                return 1 if s != "0" else 0
            count, i = 0, 0
            while i < len(s) and 1 <= int(s[:i + 1]) <= 26:
                count += solve(s[i + 1:], d)
                i += 1
            d[s] = count
            return d[s]
        
        if not s:
            return 0
        return solve(s, {})
                         