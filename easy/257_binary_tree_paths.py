# 257. Binary Tree Paths
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-paths/
# Time: O(n) | Space: O(n)
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS, build path string
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, f'{path}->{node.left.val}')
            if node.right:
                dfs(node.right, f'{path}->{node.right.val}')

        dfs(root, f'{root.val}')
        return result


# Optimized version – iterative DFS with stack
class SolutionIterative:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        stack = [(root, f'{root.val}')]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                result.append(path)
            if node.right:
                stack.append((node.right, f'{path}->{node.right.val}'))
            if node.left:
                stack.append((node.left, f'{path}->{node.left.val}'))

        return result
