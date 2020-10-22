class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Time Complexity: O(K * N) Where K is smallest positive integer that's missing and N is length of nums
        # Space Complexity: O(1)
        # i = 1
        # while True:
        #     flag = False
        #     for num in nums:
        #         if num == i:
        #             flag = True
        #             break
        #     if flag:
        #         i += 1
        #     else:
        #         return i



        # Time Complexity: O(N + K) Where K is smallest positive integer that's missing and N is length of nums
        # Space Complexity: O(N)
        # d = {}
        # for i in range(len(nums)):
        #     d[nums[i]] = i
        # i = 1
        # while True:
        #     if i in d:
        #         i += 1
        #     else:
        #         return i
        
        # Time Complexity: O(N)`
        # Space Complexity: O(1)
        # https://www.youtube.com/watch?v=9SnkdYXNIzM`
        
        if not nums:
            return 1
        
        containsone = False
        for i, num in enumerate(nums):
            if nums[i] == 1:
                containsone = True
            if nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = 1
                
        if not containsone:
            return 1
        
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] > 0 :
                nums[index] = -nums[index]
                
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        
        return len(nums) + 1