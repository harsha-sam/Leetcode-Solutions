# Medium
# REFER https://leetcode.com/problems/sum-of-two-integers/discuss/377906/easy-peasy-python(comments-works-for-negative)-solution-using-bit
# TC: O(1)
# SC: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask: 
            a, b = a^b, (a&b) << 1
        return a & mask if b > mask else a