# Easy
# https://leetcode.com/problems/palindrome-number/
# Time Complexity: O(log(x) to base 10)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        return rev == x