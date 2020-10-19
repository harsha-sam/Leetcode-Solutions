# Easy
# https://leetcode.com/problems/reverse-integer/
# Time Complexity : O(log(x) to base 10)
# Space Complexity: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        res = 0
        while temp > 0:
            res = res * 10 + temp % 10
            temp //= 10 
        if x < 0:
            res = 0 - res
        if -2 ** 31 < res < 2 **31 - 1:
            return res
        return 0