# Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast, prev = head, head, head
        # Runner Technique
        for _ in range(n):
            fast = fast.next
            if not fast:
                return head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        del slow
        return head