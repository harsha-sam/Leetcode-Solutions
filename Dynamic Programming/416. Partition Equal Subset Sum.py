# Medium
# https://leetcode.com/problems/partition-equal-subset-sum/

# TC: O(n * (sum(nums) // 2))
# SC: O(sum(nums) // 2)  
# (We can just store one array which depicts previous row, instead of entire matrix)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumi = sum(nums)
        if sumi % 2 != 0:
            return False
        target = sumi // 2     
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if j == 0:
                    dp[j] = True
                elif nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
            if dp[-1]:
                return True
        return dp[-1]

# TC: O(n * (sum(nums) // 2))
# SC: O(n * (sum(nums) // 2))
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         sumi = sum(nums)
#         if sumi % 2 != 0:
#             return False
#         target = sumi // 2                  
#         dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
#         for i in range(len(nums)):
#             for j in range(target + 1):
#                 if j == 0:
#                     dp[i][j] = True
#                 elif i == 0 and nums[i] == j:
#                     dp[i][j] = True
#                 elif i > 0 and nums[i] <= j:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#             if dp[i][-1]:
#                 return True
#         return dp[-1][-1]
    