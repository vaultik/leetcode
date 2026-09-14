# 146. LRU Cache
# Difficulty: Medium
# https://leetcode.com/problems/lru-cache/
# Time: O(1) get/put | Space: O(capacity)
from collections import OrderedDict


# My solution – OrderedDict (built-in LRU behaviour)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


# Optimized version – doubly linked list + dict, explicit O(1) control
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCacheManual:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        last_node = self.tail.prev
        node.next = self.tail
        node.prev = last_node
        last_node.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self._remove(node)
            self._add(node)
            return
        if len(self.dict) >= self.capacity:
            old_node = self.head.next
            self._remove(old_node)
            del self.dict[old_node.key]
        new_node = Node(key, value)
        self._add(new_node)
        self.dict[key] = new_node
