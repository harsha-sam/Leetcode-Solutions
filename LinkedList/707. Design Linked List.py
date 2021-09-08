# Medium
# https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.next = nex
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        TC: O(n)
        SC: O(1)
        """
        curr = self.head
        while index and curr:
            curr = curr.next
            index -= 1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        TC: O(1)
        SC: O(1)
        """
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        TC: O(1)
        SC: O(1)
        """
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        TC: O(n)
        SC: O(1)
        """
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            while index - 1:
                curr = curr.next
                index -= 1
            curr.next = Node(val, curr.next)
            self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        TC: O(n)
        SC: O(1)
        """
        if index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next  
        else:
            curr = self.head
            while index - 1:
                curr = curr.next
                index -= 1
            if curr.next.next is None:
                curr.next = None
                self.tail = curr
            else:
                curr.next = curr.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
