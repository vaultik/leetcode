# 111. Minimum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Time: O(n) | Space: O(n)
from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS, handle one-child nodes explicitly
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            elif node.left is None:
                return dfs(node.right) + 1
            elif node.right is None:
                return dfs(node.left) + 1
            else:
                return min(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)


# Optimized version – BFS, stops at first leaf (faster on wide trees)
class SolutionBFS:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
