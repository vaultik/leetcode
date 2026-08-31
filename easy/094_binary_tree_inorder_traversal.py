# 94. Binary Tree Inorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Time: O(n) | Space: O(n)
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My solution – recursive DFS
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        return result


# Alternative version – iterative DFS
# Time: O(n) | Space: O(n)
class SolutionClean:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
