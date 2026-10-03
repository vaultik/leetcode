# 6. Zigzag Conversion
# Difficulty: Medium
# https://leetcode.com/problems/zigzag-conversion/
# Time: O(n) | Space: O(n)


# My solution – simulate zigzag with direction flag
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        current_row = 0
        direction = 1

        for char in s:
            if current_row == numRows - 1:
                direction = -1
            elif current_row == 0:
                direction = 1

            rows[current_row] += char
            current_row += direction

        return ''.join(rows)


# Optimized version – math-based index jumping, no simulation
class SolutionMath:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        n = len(s)
        increment = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, n, increment):
                result.append(s[i])
                if 0 < r < numRows - 1:
                    diagonal_idx = i + increment - 2 * r
                    if diagonal_idx < n:
                        result.append(s[diagonal_idx])

        return ''.join(result)
