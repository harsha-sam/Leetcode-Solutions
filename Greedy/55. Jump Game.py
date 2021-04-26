# Medium
# https://leetcode.com/problems/jump-game/
# TC: O(N)
# SC: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            nums[i] = min(i + num, len(nums) - 1)
        
        def get_next_max(curr_max_index, lis, end):
            for i in range(curr_max_index + 1, end + 1):
                if lis[i] > lis[curr_max_index]:
                    curr_max_index = i
            return curr_max_index
        
        i = 0
        while i < len(nums) - 1:
            temp = i
            i = get_next_max(i, nums, nums[i])
            if i == temp:
                if i == nums[i]:
                    return False
                i = nums[i]
        return True