# 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution – dummy node, rebuild list
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while head:
            if head.next and head.val == head.next.val:
                head = head.next
                continue

            current.next = ListNode(head.val)
            current = current.next
            head = head.next

        return dummy.next


# Optimized version – in-place, O(1) space
# Time: O(n) | Space: O(1)
class SolutionInPlace:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head