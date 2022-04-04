# Medium
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# TC: O(N)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        first_k = slow
        for _ in range(k - 1):
            first_k = first_k.next
        fast = first_k
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.val, first_k.val = first_k.val, slow.val
        return head