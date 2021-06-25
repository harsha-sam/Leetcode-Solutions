# Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/
# TC: O(n)
# SC: O(1)
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        currSum = 0
        out = math.inf
        n = len(nums)
        while i < n:
            while j < n and currSum < target:
                currSum += nums[j]
                j += 1
            if currSum >= target:
                out = min(out, j - i)
            currSum -= nums[i]
            i += 1
        return out if out != math.inf else 0
