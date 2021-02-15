# Medium
# https://leetcode.com/problems/3sum/
# Time Complexity: O(N LOG N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            target = -nums[i]
            # To find unique triplets             
            if i == 0 or nums[i] != nums[i-1]:
                while low < high:
                    if nums[low] + nums[high] == target:
                        out.append([nums[i], nums[low], nums[high]])
                        # Update low and high to skip all the same values from   
                        # current indices                              current indices             
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1
        return out