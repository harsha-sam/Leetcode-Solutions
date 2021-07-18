# Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# TC: O(N)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        sentinel = ListNode(0, head)
        pt1 = sentinel
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if pt1.next == head:  # no duplicates
                pt1 = pt1.next
                head = head.next
            else:  # duplicates
                head = head.next
                pt1.next = head
        return sentinel.next
