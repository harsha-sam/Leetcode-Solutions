# Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def solve(l, h):
            nonlocal i
            if l > h:
                return None
            node = TreeNode(preorder[i])
            i += 1
            if l == h:
                return node
            idx = map_index[node.val]
            node.left = solve(l, idx - 1)
            node.right = solve(idx + 1, h)
            return node

        i = 0
        map_index = {inorder[i]: i for i in range(len(inorder))}
        return solve(0, len(preorder) - 1)
