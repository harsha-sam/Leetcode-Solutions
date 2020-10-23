# Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  Using BFS
class Solution:
    from queue import Queue
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = Queue()
        q.put(root)
        out = 0
        while q.qsize() > 0:
            size = q.qsize()
            out += 1
            for _ in range(size):
                s = q.get()
                if not s.left and not s.right:
                    return out
                if s.left:
                    q.put(s.left)
                if s.right:
                    q.put(s.right)     
# Using DFS
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root:
#             return self.depth(root) + 1
#         return 0
    
#     def depth(self, node):
#         if node.left and node.right:
#             return min(self.depth(node.left), self.depth(node.right)) + 1
#         elif node.left:
#             return self.depth(node.left) + 1
#         elif node.right:
#             return self.depth(node.right) + 1
#         else: 
#             return 0            
        