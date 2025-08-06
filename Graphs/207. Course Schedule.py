# Medium
# https://leetcode.com/problems/course-schedule/

# Time Complexity: O(V + E)
# Space Complexity: O(V)
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: # visiting
                return False
            elif state[node] == 2:  # visited
                return True

            state[node] = 1 # mark the current node as visiting

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True
