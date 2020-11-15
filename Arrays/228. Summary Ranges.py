# Easy
# https://leetcode.com/problems/summary-ranges/
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i + 1] - nums[i] <= 1:
                i += 1
            if nums[start] != nums[i]:
                out.append(f"{nums[start]}->{nums[i]}")
            else:
                out.append(f"{nums[start]}")
            i += 1 
        return out
                
                
            