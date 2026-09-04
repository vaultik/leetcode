# 145. Binary Tree Postorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Time: O(n) | Space: O(n)
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – iterative DFS with reverse
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        result.reverse()

        return result


# Alternative version – recursive DFS
# Time: O(n) | Space: O(n)
class SolutionClean:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)

        return result
