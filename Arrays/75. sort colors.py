# https://leetcode.com/problems/sort-colors/
# Medium
# Arrays, Two Pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(2N)    
        # Space Complexity: O(3)

        # d = {0:0, 1:0, 2:0}
        # for num in nums:
        #     d[num] += 1
        # for i in range(d[0]):
        #     nums[i] = 0
        # for i in range(d[0], d[0] + d[1]):
        #     nums[i] = 1
        # for i in range((d[0] + d[1]), d[0] + d[1] + d[2]):
        #     nums[i] = 2
        
        # Time complexity: O(2N)    
        # Space Complexity: O(1)

        # lt,n = 0, len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         nums[lt], nums[i] = nums[i], nums[lt]
        #         lt += 1
        # for i in range(lt, n):
        #     if nums[i] == 1:
        #         nums[lt], nums[i] = nums[i], nums[lt]
        #         lt += 1

        # One Pass Solution
        # Time complexity: O(N)    
        # Space Complexity: O(1)

        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
            else:
                m += 1
        