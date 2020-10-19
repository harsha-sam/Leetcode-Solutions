# Easy
# https://leetcode.com/problems/majority-element/
# Time Complexity: O(NlgN)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > len(nums) // 2:
                return num