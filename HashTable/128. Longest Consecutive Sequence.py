# Hard
# https://leetcode.com/problems/longest-consecutive-sequence/
# TC: O(N)
# SC: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = 1
        max_count = 0
        for num in d:
            if num - 1 not in d:
                temp, count = num, 1
                while temp + 1 in d:
                    temp += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count
    