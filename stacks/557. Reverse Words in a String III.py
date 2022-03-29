# Easy
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# TC: O(N)
# SC: O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res = ''
        i = 0
        while i < len(s):
            if s[i] == ' ':
                while stack:
                    res += stack.pop()
                res += ' '
            else:
                stack.append(s[i])
            i += 1
        while stack:
            res += stack.pop()
        return res
