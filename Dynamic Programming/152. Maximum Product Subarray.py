# Medium
# https://leetcode.com/problems/maximum-product-subarray/
# Modified Kadane's algorithm
# TC: O(N)
# SC: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini, out = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            temp = maxi
            maxi = max(num, num * maxi, num * mini)
            mini = min(num, num * temp, num*mini)
            print(maxi, mini)
            out = max(out, maxi)
        return out
