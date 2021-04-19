# Hard
# https://leetcode.com/problems/find-the-closest-palindrome/
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # Power of 10 case:
        # 100 -> 101, 99
        # 1000 -> 1001, 999
        temp = int(n)
        if len(n) > 1 and n[0] == '1' and n[1:] == '0' * (len(n) - 1):
            a = int(n[0] + '0' * (len(n) - 2) + '1')
            b = int(str(temp - 1))
            c = int(n)
        else:
            # All 9's Case
            # 99 next smallest palindrome = (n + 2) -> 101
            # 999 next smallest palindrome = (n + 2) -> 1001
            if n == '9' * len(n):
                a = int(str(temp + 2))
            # (Power of 10) + 1 case:
            # 101 prev smallest palindrome = (n - 2) -> 99
            # 1001 prev smallest palindrome = (n - 2) -> 999
            elif n == '1' + '0' * (len(n) - 2) + '1':
                b = int(str(temp - 2))

            # Odd length
            # Consider Prefix of (len(n) // 2) + 1 length
            # n = 12345
            # -> Prefix_len = 5 // 2 = 2
            # -> prefix = n[:Prefix_len + 1] = 123
            # Palidromes will be formed by prefix + 1, prefix - 1, prefix
            # i.e : 123 + 1 = 124 Palindrome : 12421
            # 123 - 1 = 122 Palindrome : 12221
            # 123 Palindrome : 12321
            if len(n) % 2 != 0:
                prefix = n[:(len(n) // 2) + 1]
                if not n == '9' * len(n):
                    a = str(int(prefix) + 1)
                    a = int(a + a[-2::-1])
                if not n == '1' + '0' * (len(n) - 2) + '1':
                    b = str(int(prefix) - 1)
                    b = int(b + b[-2::-1])
                c = n[:len(n) // 2 + 1]
                c = int(c + c[-2::-1])

            # Even length
            # Consider Prefix of (len(n) // 2) length
            # n = 1234
            # -> Prefix_len = 4 // 2 = 2
            # -> prefix = n[:Prefix_len] = 12
            # Palidromes will be formed by prefix + 1, prefix - 1, prefix
            # i.e : 12 + 1 = 13 Palindrome : 1331
            # 12 - 1 = 122 Palindrome : 1111
            # 12 Palindrome : 1221
            else:
                prefix = n[:(len(n) // 2)]
                if not n == '9' * len(n):
                    a = str(int(prefix) + 1)
                    a = int(a + a[::-1])
                if not n == '1' + '0' * (len(n) - 2) + '1':
                    b = str(int(prefix) - 1)
                    b = int(b + b[::-1])
                c = n[:len(n) // 2]
                c = int(c + c[::-1])
        a_diff = abs(temp - a)
        b_diff = abs(temp - b)
        c_diff = abs(temp - c)
        if c_diff != 0:
            min_diff = min(a_diff, b_diff, c_diff)
        else:
            min_diff = min(a_diff, b_diff)
        out = a
        if min_diff == a_diff:
            out = a
        if min_diff == b_diff:
            out = min(out, b)
        if min_diff == c_diff:
            out = min(out, c)
        return str(out)
