# Hard
# https://leetcode.com/problems/minimum-window-substring/
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for char in t:
            d[char] = d.get(char, 0) + 1
        start, end = 0, 0
        number_of_chars_req = len(t)
        minimum = ""
        while end < len(s):
            # print("in", start, end, s[start:end + 1])
            if s[end] in d:
                # print("char is needed", s[end])
                if d[s[end]] > 0:
                    number_of_chars_req -= 1
                d[s[end]] -= 1
                # print("d", d, number_of_chars_req)
            while number_of_chars_req == 0:
                # print("req chars is zero", start, end, s[start:end])
                if end - start + 1 < len(minimum) or not minimum:
                    # print("found", s[start:end])
                    minimum = s[start: end + 1]
                if s[start] in d:
                    # print("char is needed s", s[start])
                    d[s[start]] += 1
                    if d[s[start]] > 0:
                        number_of_chars_req += 1
                    # print("s d", d, number_of_chars_req)
                start += 1
            end += 1
        return minimum