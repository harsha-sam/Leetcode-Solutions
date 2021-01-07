#  Hard
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    def serialize(self, root):
        # Time Complexity: O(N) 
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        q = Queue()
        q.put(root)
        out = ""
        while q.qsize():
            node = q.get()
            if node:
                out += str(node.val) + ","
                q.put(node.left if node.left else None)
                q.put(node.right if node.right else None)
            else:
                out += "null,"
        return out       

    def deserialize(self, data):
        # Time Complexity: O(N) 
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """ 
        if not data:
            return None
        
        data = data.split(',')[:-1]
        q = Queue()
        val = int(data[0])
        root = TreeNode(val) 
        q.put(root)
        i = 1
        while i < len(data):
            node = q.get()
            if data[i] != 'null':
                val = int(data[i])
                left = TreeNode(val)
                node.left = left
                q.put(left)
            if data[i + 1] != 'null':
                val = int(data[i + 1])
                right = TreeNode(val)
                node.right = right
                q.put(right)
            i += 2
        return root
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))