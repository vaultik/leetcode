# 21. Merge Two Sorted Lists
# Difficulty: Easy
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1 — first attempt (O(n+m) time | O(n+m) space)
class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def to_list(l):
            values = []
            current = l
            while current:
                values.append(current.val)
                current = current.next
            return values

        result = sorted(to_list(list1) + to_list(list2))

        dummy = ListNode(0)
        current = dummy
        for r in result:
            current.next = ListNode(r)
            current = current.next
        return dummy.next


# Solution 2 — optimized in-place (O(n+m) time | O(1) space)
class Solution2:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return dummy.next
