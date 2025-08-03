# Easy
# https://leetcode.com/problems/valid-anagram/

# Time Complexity : O(n log n) using sorting
# class Solution:     
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# Time Complexity : O(n) 
# Space Complexity : O(n)
class Solution:     
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1

        return all(v == 0 for v in d.values())
