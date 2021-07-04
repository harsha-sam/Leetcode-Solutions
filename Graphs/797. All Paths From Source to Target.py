# Medium
# https: // leetcode.com/problems/all-paths-from-source-to-target/
# DFS
# TC: O(V * V)
# The time complexity is polynomial.
# From each vertex there are v vertices that can be visited from current vertex.
# SC: O(V * V)
# To store the paths V^V space is needed.

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(u, dest, curr_path):
            vis[u] = True
            curr_path.append(u)
            if u == dest:
                all_paths.append(curr_path.copy())
            else:
                for v in graph[u]:
                    if not vis[v]:
                        dfs(v, dest, curr_path)
            vis[u] = False
            curr_path.pop()
        
        vis = [False for _ in range(len(graph))]
        all_paths = []
        dfs(0, len(graph) - 1, [])
        return all_paths
