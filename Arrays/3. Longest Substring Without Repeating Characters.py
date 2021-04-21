# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach: Sliding Window
# References : 
# https://www.youtube.com/watch?v=s2ZGeNeKpuI (Maximum Window Substring)
# https://www.youtube.com/watch?v=eS6PZLjoaq8 (Minimum Window Substring)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        for char in s:
            hash_map[char] = 0
        start, end = 0, 0
        longest_substring = 0
        while start < len(s):
            if hash_map[s[start]] > 0:
                hash_map[s[start]] -= 1
                start += 1
            while end < len(s) and hash_map[s[end]] == 0:
                hash_map[s[end]] += 1
                end += 1
            longest_substring = max(longest_substring, end - start)
        return longest_substring