# Easy
# https://leetcode.com/problems/min-stack/
# All operations time complexity : O(1)
# Space Complexity: O(N)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        if not self.stack:
            self.min.append(x)
        self.stack.append(x)
        self.min.append(x) if x < self.min[-1] else self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()