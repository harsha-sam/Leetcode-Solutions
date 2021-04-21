# Easy
# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while not n in d:
            d[n] = 1
            sum_of_squares_of_digits = 0
            while n > 0:
                sum_of_squares_of_digits += (n % 10) ** 2
                n //= 10
            n = sum_of_squares_of_digits
        return n == 1
                
