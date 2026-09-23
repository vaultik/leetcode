# 112. Path Sum
# Difficulty: Easy
# https://leetcode.com/problems/path-sum/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS, subtract node value at each step
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, differ):
            if node is None:
                return False
            if node.left is None and node.right is None and differ - node.val == 0:
                return True

            differ -= node.val
            return dfs(node.left, differ) or dfs(node.right, differ)

        return dfs(root, targetSum)


# Optimized version – iterative DFS with stack
class SolutionIterative:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right and curr_sum == 0:
                return True

            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

        return False
