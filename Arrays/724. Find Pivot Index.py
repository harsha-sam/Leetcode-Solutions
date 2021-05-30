# Easy
# https://leetcode.com/problems/find-pivot-index/
# Time Complexity : O(N)
# Space Complexity : O(1)
# Approach : Prefix Sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        if len(nums) == 1 or s - nums[0] == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] == s - nums[i - 1] - nums[i]:
                return i
            nums[i] += nums[i - 1]
        return -1