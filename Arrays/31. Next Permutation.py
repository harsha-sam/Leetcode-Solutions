# Medium
# https://leetcode.com/problems/next-permutation/

# https://www.youtube.com/watch?v=quAS1iydq7U

# TC: O(N)
# SC: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # if a sequence is decreasing, then we can say that it exhausted all it's possibilities. Find a place where this is breaking and swap with the smallest greater element
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i
                break
        if index == -1:
            self.reverseList(0, len(nums) - 1, nums)
        else:
            mini_max = index - 1
            for i in range(len(nums) - 1, index - 1, -1):
                if nums[i] > nums[index - 1]:
                    mini_max = i
                    break
            nums[index - 1], nums[mini_max] = nums[mini_max], nums[index - 1]
            self.reverseList(index, len(nums) - 1, nums)

    def reverseList(self, start_index, end_index, l):
        i, j = start_index, end_index
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
