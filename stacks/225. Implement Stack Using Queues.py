# Easy
# https://leetcode.com/problems/implement-stack-using-queues/

# TC: 
# Push: O(1)
# Pop: O(n)
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        size = len(self.q1)
        for _ in range(size - 1):
            val = self.q1.popleft()
            self.push(val)
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return None
        val = self.pop()
        self.push(val)
        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()