# 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Time: O(n*m) | Space: O(1)
import re


# My solution – regex search
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        return match.start() if match else -1


# Optimized version – sliding window
# Time: O(n*m) | Space: O(1)
class SolutionSliding:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        for i in range(h_len - n_len + 1):
            if haystack[i : i + n_len] == needle:
                return i
        return -1


# Pythonic version – built-in find
class SolutionBuiltin:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)