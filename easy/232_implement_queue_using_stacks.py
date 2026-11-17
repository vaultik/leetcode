# 232. Implement Queue using Stacks
# Difficulty: Easy
# https://leetcode.com/problems/implement-queue-using-stacks/
# Time: O(1) amortized | Space: O(n)


# My solution – two stacks, lazy transfer
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move_elements()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _move_elements(self) -> None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Alternative – eager transfer on push
class MyQueueEager:
    def __init__(self):
        self.main_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        while self.main_stack:
            self.temp_stack.append(self.main_stack.pop())
        self.main_stack.append(x)
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return not self.main_stack
