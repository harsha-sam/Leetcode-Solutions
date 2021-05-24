"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Medium
# https://leetcode.com/problems/clone-graph/
# TC:O(n) -> As we are doing dfs and we'll visit each node just once
# SC:O(n) -> recursion stack and memoization of nodes
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def explore(v, d):
            if not v:
                return None
            head = Node(v.val, [])
            d[head.val] = head
            for u in v.neighbors:
                if u.val in d:
                    head.neighbors.append(d[u.val])
                else:
                    head.neighbors.append(explore(u, d))
            return head
        return explore(node, {})
                    