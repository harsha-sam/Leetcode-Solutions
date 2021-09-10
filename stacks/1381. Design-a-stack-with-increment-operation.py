# Medium
# https://leetcode.com/problems/design-a-stack-with-increment-operation/
# TC: PUSH O(1) ; POP O(1) ; Increment O(1)
# SC: O(N)

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.offset = []
        self.size = maxSize

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) >= self.size

    def push(self, x: int) -> None:
        if not self.isFull():
            self.stack.append(x)
            self.offset.append(0)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        top_element = self.stack.pop()
        top_offset = self.offset.pop()
        if not self.isEmpty():
            self.offset[-1] += top_offset
        return top_element + top_offset

    def increment(self, k: int, val: int) -> None:
        if not self.isEmpty():
            k = min(k, len(self.stack))
            self.offset[k - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
