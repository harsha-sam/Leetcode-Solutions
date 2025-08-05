"""
      Finds the k closest points to the origin (0, 0).
        Logic:
        - We keep a max-heap (priority queue) limited to size k to store the closest points seen so far.
        - Each heap entry stores the negative squared distance and the point, so the root is the farthest among the k.
        - For each new point, if the heap has fewer than k points, we add it.
        - Otherwise, if the new point is closer than the farthest point in the heap, we replace the farthest.
        - Limiting heap size to k keeps operations efficient (O(log k)) and uses minimal memory.
        - After processing all points, the heap contains exactly the k closest points.
"""
from typing import List
from collections import namedtuple
import heapq

Point = namedtuple('Point', ['x', 'y'])


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = x * x + y * y
            point = Point(x, y)
            heap_item = (-dist, point)

            if len(max_heap) < k:
                heapq.heappush(max_heap, heap_item)
            # current point is closer than farthest in heap
            elif -dist > max_heap[0][0]:
                heapq.heappushpop(max_heap, heap_item)

        return [[p.x, p.y] for _, p in max_heap]
