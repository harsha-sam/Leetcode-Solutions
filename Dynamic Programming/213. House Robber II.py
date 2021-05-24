# Medium
# https://leetcode.com/problems/house-robber-ii/
# TC: O(n)
# SC: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        elif len(nums) == 1:
            return nums[0]
        
        elif len(nums) <= 3:
            return max(nums)
        
        def houseRobberI(nums):
            a = nums[0]
            b = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                a, b = b, max(a + nums[i], b) 
            return b
        
        # find the max between 
        # houseRobberI(the head being eliminated) and 
        # houseRobberI(tail being eliminated)
        return max(houseRobberI(nums[1:]), houseRobberI(nums[:len(nums) - 1]))