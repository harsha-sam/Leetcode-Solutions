# TC: O(S + t)
# SC: O(1)
# From XOR characteristics
# 0 ^ x = x
# x ^ x = 0, x is any number
# So, if we use 0 to XOR both str s and t. The last value will be ASCII of difference character

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for char in s:
            c ^= ord(char)
        for char in t:
            c ^= ord(char)
        return chr(c)