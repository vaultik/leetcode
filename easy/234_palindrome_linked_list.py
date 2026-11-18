# 234. Palindrome Linked List
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-linked-list/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution – collect values, two pointers
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        current = head

        while current:
            check.append(current.val)
            current = current.next

        left = 0
        right = len(check) - 1

        while left < right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1

        return True


# Optimized version – find mid, reverse second half, O(1) space
# Time: O(n) | Space: O(1)
class SolutionInPlace:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        first_half = head
        second_half = prev_node

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
