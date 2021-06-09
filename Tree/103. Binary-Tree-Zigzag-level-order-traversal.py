# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)

# Approach BFS :
# Store reverse of nodes at alternate levels
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        q = deque([root])
        out = []
        while q:
            size = len(q)
            nodes = []
            for _ in range(size):
                curr = q.popleft()
                nodes.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level % 2 == 0 and nodes:
                out.append(nodes)
            elif nodes:
                out.append(nodes[::-1])
            level += 1
        return out
