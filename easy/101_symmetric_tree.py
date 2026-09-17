# 101. Symmetric Tree
# Difficulty: Easy
# https://leetcode.com/problems/symmetric-tree/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – recursive DFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)


# Optimized version – iterative with stack
class SolutionIterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [root.left, root.right]

        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            else:
                stack.append(node1.left)
                stack.append(node2.right)
                stack.append(node1.right)
                stack.append(node2.left)

        return True
