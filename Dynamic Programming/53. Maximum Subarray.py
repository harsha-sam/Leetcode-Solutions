# Easy
# https://leetcode.com/problems/maximum-subarray/
# Kadane's algorithm
# TC : O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            globalMax = max(globalMax, currMax)
        return globalMax