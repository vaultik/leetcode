# 160. Intersection of Two Linked Lists
# Difficulty: Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Time: O(n+m) | Space: O(1)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# My solution – two pointers, switch heads on None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_A = headA
        node_B = headB

        while node_A != node_B:
            if node_A is None and node_B is None:
                return None
            elif node_B is None:
                node_B = headA
            elif node_A is None:
                node_A = headB
            else:
                node_A = node_A.next
                node_B = node_B.next

        return node_A


# Optimized version – cleaner two pointers
class SolutionClean:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_A = headA
        node_B = headB

        while node_A is not node_B:
            node_A = headB if node_A is None else node_A.next
            node_B = headA if node_B is None else node_B.next

        return node_A
