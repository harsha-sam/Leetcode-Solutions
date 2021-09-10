# Medium

# LRU Cache with Hash_map and DLL
# TC: get: O(1) ; put: O(1)
# SC: Hash_map(capacity), DLL(capacity + 2)

# References:
# https://www.youtube.com/watch?v=xDEuM5qa0zg

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.key}:{self.val}'


class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.size = capacity
        # creating dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.delete_node(node)
            self.insert_begin(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.delete_node(node)
            del self.hash_map[key]

        elif len(self.hash_map) == self.size:
            lru_node = self.tail.prev
            self.delete_node(lru_node)
            del self.hash_map[lru_node.key]

        new_node = Node(key, value)
        self.hash_map[key] = new_node
        self.insert_begin(new_node)

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_begin(self, node):
        head = self.head
        node.prev = head
        node.next = head.next
        head.next.prev = node
        head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
