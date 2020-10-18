# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Medium

class Solution:
#   Linear search : O(n)
#   Space Complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        flag = 0
        for index, ele in enumerate(nums):
            if ele == target: 
                if not flag:
                    start = index
                    end = index
                    flag = 1
                else:
                    end = index
        return start, end


# Binary search
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Finding first pos         
        l = 0
        h = len(nums) - 1
        pos = [-1, -1]
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                pos[0] = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        # Finding last pos                         
        if pos[0] != -1:                  
            l = pos[0]
            h = len(nums) - 1
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    pos[1] = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
        return pos
                
        