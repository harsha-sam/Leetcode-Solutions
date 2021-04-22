# Medium
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
# TC: O(N)
# SC: O(1)
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for num in arr:
            target_rem = k - (num % k)
            if target_rem == k:
                target_rem = 0
            if target_rem in d:
                d[target_rem] -= 1
                if d[target_rem] == 0:
                    del d[target_rem]
            else:
                d[num % k] = d.get(num % k, 0) + 1
        return not d

# arr = [1,2,3,4,5,10,6,7,8,9]  k = 5
# Explanation : Store frequency of remainders
# 1 - rem : 1 
# 2 - rem : 2 and so on..
# if for a number i which has remainder r1 when divided by k, 
# check if r2 = k - r1 exists in the hash_table (i.e there exists a number j which leaves remainder r2) 
# because the sum of both i + j will be exactly divided by k
# Example : 2 % 5 leaves remainder r1 - 2, now target = k - r1 = 5 - 2 = 3
# Remainder 3 exists because 3 % 5 leaves remainder r2 - 3 and i + j = 2 + 3 = 5 is divided by 5 (K)
# Handle a case when r1 = 0, target should be 0
