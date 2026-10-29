# 24. Swap Nodes in Pairs
# Difficulty: Medium
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Time: O(n) | Space: O(1)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution – iterative with dummy node
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            current.next = second
            first.next = second.next
            second.next = first
            current = first

        return dummy.next


# Optimized version – recursive
class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node
