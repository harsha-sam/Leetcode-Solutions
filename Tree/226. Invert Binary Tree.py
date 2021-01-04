# Easy
# https://leetcode.com/problems/invert-binary-tree/
# Time Complexity: O(N)
# Space Complexity: O(N)
from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        # return self.iterative_invert(root)
        return root
    
    # recursive     
    def helper(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.helper(node.left)
            self.helper(node.right)
    
    # iterative - bfs approach
    def iterative_invert(self, root):
        if root:
            q = Queue()
            q.put(root)
            while q.qsize() > 0:
                node = q.get()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return root
            