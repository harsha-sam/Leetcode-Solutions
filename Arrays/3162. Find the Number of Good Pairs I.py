from bisect import bisect_left


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        nums1.sort()
        nums2 = [num * k for num in nums2]
        count = 0
        for j in range(len(nums2)):
           idx = bisect_left(nums1, nums2[j])
           for i in range(idx, len(nums1)):
               if nums1[i] % nums2[j] == 0:
                   count += 1
        return count
