# 100. Same Tree
# Difficulty: Easy
# https://leetcode.com/problems/same-tree/
# Time: O(n) | Space: O(n)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution – DFS, serialize both trees and compare
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = []

        def dfs(node):
            if node is None:
                result.append('None')
                return
            dfs(node.right)
            dfs(node.left)
            result.append(node.val)

        dfs(p)
        first, result = result, []
        dfs(q)

        return True if first == result else False


# Optimized version – recursive comparison, early exit
class SolutionClean:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
