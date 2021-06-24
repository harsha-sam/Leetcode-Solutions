# Medium
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# TC: O(n)
# SC: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = deque([root])
        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if prev:
                    prev.next = node
                prev = node
        return root
