# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: Sliding Window
# References : 
# https://www.youtube.com/watch?v=s2ZGeNeKpuI (Maximum Window Substring)
# https://www.youtube.com/watch?v=eS6PZLjoaq8 (Minimum Window Substring)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            while r < len(s) and count.get(s[r], 0) == 0:
                count[s[r]] = count.get(s[r], 0) + 1
                r += 1
            maxLen = max(maxLen, r-l)
            count[s[l]] = count.get(s[l]) - 1
            l += 1

        return maxLen
