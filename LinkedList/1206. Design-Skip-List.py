# Hard
# https://leetcode.com/problems/design-skiplist/

# References:
# https://www.youtube.com/watch?v=UGaOXaXAM5M
# https://leetcode.com/problems/design-skiplist/discuss/1082053/simple-solution-with-dynamic-levels
# https://cw.fel.cvut.cz/old/_media/courses/a4b36acm/maraton2015skiplist.pdf

from math import inf
import random


class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.next = nex
        self.down = None


class Skiplist:

    def __init__(self):
        sentinel = Node(-inf, Node(inf))
        self.levels = [sentinel]

    def search(self, target: int) -> bool:
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < target:
                node = node.next
            if node.next.val == target:
                return True
            level = node.down
        return False

    def add(self, num: int) -> None:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            stack.append(node)
            level = node.down

        heads = True
        down = None
        while stack and heads:
            prev = stack.pop()
            node = Node(num, prev.next)
            node.down = down
            prev.next = node
            down = node
            heads = random.randint(0, 1)

        # adding new level if we got all heads till top
        if heads:
            node = Node(-inf, Node(num))
            node.down = self.levels[-1]
            node.next.next = Node(inf)
            node.next.down = down
            self.levels.append(node)

    def erase(self, num: int) -> bool:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            if node.next.val == num:
                stack.append(node)
            level = node.down

        if not stack:
            return False

        for node in stack:
            node.next = node.next.next

        # removing empty top layers
        while len(self.levels) > 1 and self.levels[-1].next.next is None:
            self.levels.pop()

        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
