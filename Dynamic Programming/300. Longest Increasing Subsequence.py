# Medium
# https://leetcode.com/problems/longest-increasing-subsequence
# https://www.youtube.com/watch?v=odrfUCS9sQk

# TC: O(n ** 2)
# SC: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        out = 0
        for i in range(len(nums)):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, dp[j])
            dp.append(maxi + 1)
            out = max(out, dp[i])
        return out