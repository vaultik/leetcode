# 144. Binary Tree Preorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Time: O(n) | Space: O(n)
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result


# Alternative version – iterative DFS
# Time: O(n) | Space: O(n)
class SolutionClean:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
