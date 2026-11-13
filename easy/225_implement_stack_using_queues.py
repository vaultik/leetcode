# 225. Implement Stack using Queues
# Difficulty: Easy
# https://leetcode.com/problems/implement-stack-using-queues/
# Time: O(n) push, O(1) pop/top | Space: O(n)
from collections import deque


# My solution – list with rotate on push
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        length = len(self.stack)
        self.stack.append(x)
        for _ in range(length):
            self.stack.append(self.stack.pop(0))

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0)

    def top(self) -> int:
        if not self.empty():
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Optimized version – deque with rotate on push
class MyStackDeque:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        length = len(self.queue)
        self.queue.append(x)
        for _ in range(length):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
