# 141. Linked List Cycle
# Difficulty: Easy
# https://leetcode.com/problems/linked-list-cycle/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# My solution – hash set of visited nodes
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        result = set()

        while head:
            if head in result:
                return True
            result.add(head)
            head = head.next

        return False


# Optimized version – Floyd's cycle detection (two pointers), O(1) space
# Time: O(n) | Space: O(1)
class SolutionFloyd:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
