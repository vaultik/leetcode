# 108. Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Time: O(n) | Space: O(n)
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – slice arrays recursively
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid_idx = len(nums) // 2
        root_node = TreeNode(nums[mid_idx])
        left = nums[:mid_idx]
        right = nums[mid_idx + 1:]

        root_node.left = self.sortedArrayToBST(left)
        root_node.right = self.sortedArrayToBST(right)

        return root_node


# Optimized version – index pointers, no slicing, O(1) extra space per call
class SolutionPointers:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = convert(left, mid - 1)
            root.right = convert(mid + 1, right)

            return root

        return convert(0, len(nums) - 1)
