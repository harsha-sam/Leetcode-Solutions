# Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Time Complexity: O(N) Inorder Traversal
# Space Complexity: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return None
            nonlocal k
            left = inorder(node.left)
            if left is not None:
                return left
            k -= 1
            if k == 0:
                return node.val
            return inorder(node.right)

        ans = inorder(root)
        if ans is None:
            return -1
        return ans

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         def inorder(node, order):
#             if node:
#                 inorder(node.left, order)
#                 order.append(node.val)
#                 inorder(node.right, order)
        
#         order = []
#         inorder(root, order)
#         return order[k - 1]
