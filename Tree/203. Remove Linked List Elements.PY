# Easy
# https://leetcode.com/problems/remove-linked-list-elements/

# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            temp, prev = head, None                
            while temp:
                if temp.val == val:
                    if not prev:
                        head = head.next
                    else:
                        prev.next = temp.next
                else:
                    prev = temp
                temp = temp.next
        return head