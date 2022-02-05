# Medium
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def solve(curr):
            nonlocal k, res
            if len(curr) > n or k == 0 or (len(curr) > 1 and curr[-1] == curr[-2]):
                return
            if len(curr) == n:
                k -= 1
            if k == 0:
                res = curr
            solve(curr + 'a')
            solve(curr + 'b')
            solve(curr + 'c')

        res = ''
        solve('')
        return res
