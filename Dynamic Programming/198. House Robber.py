# Medium
# https://leetcode.com/problems/house-robber/

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i-1])
        return dp[i]
    
class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b) 
        return b