# Easy
# https://leetcode.com/problems/intersection-of-two-arrays/
# Time Complexity: O(n + m) 
# Space Complexity: O(n + m)
# where n = len(nums1) and m = len(nums2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        d2 = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        for num in nums2:
            d2[num] = d2.get(num, 0) + 1
        return [num for num in d2.keys() if num in d]
                