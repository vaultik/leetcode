# 66. Plus One
# Difficulty: Easy
# https://leetcode.com/problems/plus-one/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – reverse traversal with carry
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        n = -1
        while digits[n] == 9:
            if n == -len(digits):
                digits[n] = 0
                return [1] + digits
            digits[n] = 0
            n -= 1
        digits[n] += 1
        return digits


# Optimized version – cleaner reverse traversal
class SolutionClean:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits