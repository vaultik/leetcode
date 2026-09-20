# 110. Balanced Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/balanced-binary-tree/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – DFS, return -1 as sentinel for unbalanced
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(node):
            if node is None:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1

        return dfs(root) != -1


# Optimized version – return (is_balanced, height) tuple, more explicit
class SolutionTuple:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return (True, 0)

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )
            height = max(left_height, right_height) + 1

            return (balanced, height)

        return dfs(root)[0]
