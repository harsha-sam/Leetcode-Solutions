# Medium
# https://leetcode.com/problems/split-linked-list-in-parts/

# Time Complexity: O(max(k, n))
# Space Complexity: O(K)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        size = 0
        head = root
        # Finds the length of linkedlist         
        while head:
            head = head.next
            size += 1
        # If there are N nodes in the linked list root, then there are N/K               items in each part,   
        part_len = [round(size / k) for _ in range(k)]
        # There can be N % K items remaining
        # Remaining can be < 0 as I'm rounding the division         
        rem = size - part_len[0] * k 
        i = 0
        # If remaining items > 0         
        while rem > 0:
            if i == k - 1:
                i = 0
            part_len[i] += 1
            rem -= 1
            i += 1
        # If remaining items < 0
        i = k - 1
        while rem < 0:
            if i == 0:
                i = k - 1
            part_len[i] -= 1
            rem += 1
            i -= 1
        out = []
        head = root
        # Splitting into parts based on the part_lengths list         
        for i in range(k):
            start = head
            for _ in range(part_len[i]-1):
                if head:
                    head = head.next
                else:
                    break
            if head:
                end = head
                head = head.next
                end.next = None
            out.append(start)
        return out
        