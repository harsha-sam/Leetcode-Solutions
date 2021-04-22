# Medium
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        # print(prev)
        for _ in range(n-1):
            i = 0
            res = ''
            while i < len(prev):
                c = 1
                while i+1 < len(prev) and prev[i] == prev[i+1]:
                    c += 1
                    i += 1
                res += str(c) + prev[i]
                i += 1
            # print(res)
            prev = res
        return prev                