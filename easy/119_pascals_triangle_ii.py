# 119. Pascal's Triangle II
# Difficulty: Easy
# https://leetcode.com/problems/pascals-triangle-ii/
# Time: O(n²) | Space: O(n)
from typing import List


# My solution – build all rows, return last
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1] * x for x in range(1, rowIndex + 2)]

        current = 2
        idx = 1

        while current <= rowIndex:
            if idx >= len(result[current - 1]):
                current += 1
                idx = 1
                continue

            result[current][idx] = result[current - 1][idx - 1] + result[current - 1][idx]
            idx += 1

        return result[-1]


# Optimized version – single row, O(n) space
class SolutionClean:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            row = [a + b for a, b in zip([0] + row, row + [0])]

        return row
