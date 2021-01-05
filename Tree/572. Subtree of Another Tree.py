# Easy
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N * M) - Where M = number of nodes in subtree t and N = number of nodes in tree s
# Space Complexity: O(N) - Depth in recursion can go upto n nodes. n refers to number of nodes in s.
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check_equal(tree1, tree2):
            if tree1 and not tree2 or tree2 and not tree1:
                return False
            elif tree1 and tree2:
                if tree1.val != tree2.val:
                    return False
                if not check_equal(tree1.left, tree2.left):
                    return False
                if not check_equal(tree1.right, tree2.right):
                    return False
            return True

        def explore(curr, t):
            if curr:
                if curr.val == t.val and check_equal(curr, t):
                    return True
                if explore(curr.left, t):
                    return True
                if explore(curr.right, t):
                    return True

        return explore(s, t)
