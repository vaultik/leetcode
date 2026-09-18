# 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS, explicit comparison
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return left_depth + 1 if left_depth > right_depth else right_depth + 1

        return dfs(root)


# Optimized version – cleaner one-liner recursion
class SolutionClean:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
