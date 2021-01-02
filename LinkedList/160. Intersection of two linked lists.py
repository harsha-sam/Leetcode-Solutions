# Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Refer CTCI PAGE 222
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time Complexity: O(N + M) where N = len(list1) and M = len(list2)
    # Space Complexity: O(1)    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def findLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        
        tempA, tempB = headA, headB
        n, m = findLength(tempA), findLength(headB)
        shorter = headA if n < m else headB
        longer = headA if n >= m else headB
        for _ in range(abs(n - m)):
            longer = longer.next
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        return longer
        