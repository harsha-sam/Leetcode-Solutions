# Easy
# https://leetcode.com/problems/implement-queue-using-stacks/
# TC: push: O(1) ; pop: amortized O(1) ; pop O(1)

# Refer
# https://leetcode.com/problems/implement-queue-using-stacks/solution/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack2:
            self.front = x
        self.stack2.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack1:
            return self.stack1[-1]
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
