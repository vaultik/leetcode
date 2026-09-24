# 118. Pascal's Triangle
# Difficulty: Easy
# https://leetcode.com/problems/pascals-triangle/
# Time: O(n²) | Space: O(n²)
from typing import List


# My solution – preallocate rows, fill inner values by index
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * x for x in range(1, numRows + 1)]

        current = 2
        idx = 1

        while current < numRows:
            if idx >= len(result[current - 1]):
                current += 1
                idx = 1
                continue

            result[current][idx] = result[current - 1][idx - 1] + result[current - 1][idx]
            idx += 1

        return result


# Optimized version – zip trick, cleaner and more Pythonic
class SolutionClean:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for _ in range(numRows - 1):
            last_row = result[-1]
            next_row = [a + b for a, b in zip([0] + last_row, last_row + [0])]
            result.append(next_row)

        return result
