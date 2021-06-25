# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = deque([root])
        out = []
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        return out[::-1]
