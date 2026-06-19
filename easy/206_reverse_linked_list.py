# 206. Reverse Linked List
# Difficulty: Easy
# https://leetcode.com/problems/reverse-linked-list/
# Time: O(n) | Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution – collect values, rebuild reversed, O(n) time, O(n) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        result = []

        while head:
            value = head.val if head else None
            result.append(value)
            head = head.next

        for v in reversed(result):
            current.next = ListNode(v)
            current = current.next

        return dummy.next


# Optimal solution – in-place reversal, O(n) time, O(1) space
class SolutionOptimal:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
