# Easy
# https://leetcode.com/problems/valid-parentheses

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in m.values():
                stack.append(ch)
            elif not stack or stack.pop() != m.get(ch):
                return False
        return not stack
