# Easy
# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        def check_ugly(n):
            if n == 0:
                return False
            elif n == 1:
                return True
            elif n % 2 == 0:
                return check_ugly(n // 2)
            elif n % 3 == 0:
                return check_ugly(n // 3)
            elif n % 5 == 0:
                return check_ugly(n // 5)
            return False
        return check_ugly(n)