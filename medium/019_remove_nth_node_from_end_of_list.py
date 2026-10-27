# 19. Remove Nth Node From End of List
# Difficulty: Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Time: O(n) | Space: O(1)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution – count length, then walk to target
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (n == 1 and head.next is None):
            return head.next

        current = head
        count = 0

        while current:
            count += 1
            current = current.next

        if count == n:
            return head.next

        diff = count - n
        current = head

        while diff:
            diff -= 1
            if diff == 0:
                current.next = current.next.next
                break
            current = current.next

        return head


# Optimized version – two pointers, one pass
class SolutionTwoPointers:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
