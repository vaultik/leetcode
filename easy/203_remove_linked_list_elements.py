# 203. Remove Linked List Elements
# Difficulty: Easy
# https://leetcode.com/problems/remove-linked-list-elements/
# Time: O(n) | Space: O(1)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution – iterative with dummy node
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = dummy.next

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next


# Optimized version – recursive
class SolutionRecursive:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
