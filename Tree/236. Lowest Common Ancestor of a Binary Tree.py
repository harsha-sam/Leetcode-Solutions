# Medium
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Complexity Analysis
# Time Complexity : O(N), where N is the number of nodes in the binary tree. 
# In the worst case we might be visiting all the nodes of the binary tree and they didn't mention the binary tree is balaned
# Space Complexity: O(N). 
# This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findParent(node, parent):
            if not node:
                return
            node.parent = parent
            findParent(node.left, node)
            findParent(node.right, node)
        
        findParent(root, None)
        
        # get p's parents
        parent1 = [ p ]
        while p.parent:
            parent1.append(p.parent)
            p = p.parent
            
        # get q's parents
        parent2 = [ q ]
        while q.parent:
            parent2.append(q.parent)
            q = q.parent
            
        # find lowest common ancestor
        i, j = len(parent1)-1, len(parent2)-1
        while i>=0 and j >=0:
            if parent1[i].val != parent2[j].val:
                break
            lca = parent1[i]
            i-=1
            j-=1
        return lca
        