# Easy
# https://leetcode.com/problems/next-greater-element-i/submissions/
# https://www.youtube.com/watch?v=sDKpIO2HGq0
# TC: O(N)
# SC: O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for num in nums1:
            d[num] = -1
        for index, num in enumerate(nums2):
            while len(stack) and num > nums2[stack[-1]]:
                ele = nums2[stack.pop()]
                if ele in d:
                    d[ele] = num
            stack.append(index)
        return [d[num] for num in nums1]
        