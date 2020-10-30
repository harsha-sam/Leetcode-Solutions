# Easy
# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        out = []
        self.explore(root, [], out)
        return out
        
    def explore(self, root, path, out):
        if root:
            path.append(root.val)
            if not root.left and not root.right:
                out.append('->'.join([str(i) for i in path]))
            self.explore(root.left, path, out)
            self.explore(root.right, path, out)
            path.pop()
        