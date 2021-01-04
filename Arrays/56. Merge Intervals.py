# Medium
# https://leetcode.com/problems/merge-intervals/

# Time Complexity: O(N log N) - sorting pts
# Space Complexity: O( N )
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []
        for pt in intervals:
            new_intervals.append((pt[0], 'l'))
            new_intervals.append((pt[1], 'r'))
        
        new_intervals.sort(key=lambda pt: (pt[0], pt[1]))
        out = []
        start = new_intervals[0][0]
        count = 0
        for pt in new_intervals:
            if pt[1] == 'l':
                count += 1
                if start == -1:
                    start = pt[0]
            elif pt[1] == 'r':
                count -= 1
                if count == 0:
                    out.append([start, pt[0]])
                    start = -1
        return out