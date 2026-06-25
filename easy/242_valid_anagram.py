# 242. Valid Anagram
# Difficulty: Easy
# https://leetcode.com/problems/valid-anagram/
# Time: O(n log n) | Space: O(n)
from collections import Counter


# My solution – sort both strings, O(n log n) time, O(n) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Optimal solution – Counter, O(n) time, O(n) space
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
