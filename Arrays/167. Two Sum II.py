# Medium
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# TC: O(N)
# SC: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1
