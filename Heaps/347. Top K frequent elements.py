# Medium
# https://leetcode.com/problems/top-k-frequent-elements/

# Time Complexity: O(N)
# Space Complexity: O(2N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums: # O(N)
            d[num] = d.get(num, 0) + 1
            
        c = {}
        maxi = 0
        for key, val in d.items():# O(N)
            c[val] = c.get(val, []) + [key]
            maxi = max(val, maxi)
        
        out = []
        for i in range(maxi, -1, -1): # O(N)`
            if len(out) >= k:
                return out[:k]
            try:
                out += c[i]
            except KeyError:
                pass
            
# Time Complexity: O(K log N)
# Space Complexity: O(N) 
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         import heapq
#         d = {}
#         for num in nums:
#             d[num] = d.get(num, 0) + 1
#         heap = []
#         for key, val in d.items():
#             heapq.heappush(heap, (-val, key))
#         return [heapq.heappop(heap)[1] for _ in range(k)]

# Time Complexity: O(N log N)
# Space Complexity: O(N) 
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         d = {}
#         for num in nums:
#             d[num] = d.get(num, 0) + 1
#         out = sorted(d.keys(), key=lambda i: d[i], reverse=True)[:k]
#         return out