# Medium
# https://leetcode.com/problems/find-bottom-left-tree-value/
# TC : O(N) 
# SC : O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft() 
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return curr.val