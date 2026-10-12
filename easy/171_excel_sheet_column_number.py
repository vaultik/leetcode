# 171. Excel Sheet Column Number
# Difficulty: Easy
# https://leetcode.com/problems/excel-sheet-column-number/
# Time: O(n) | Space: O(1)


# My solution – reverse iteration with power of 26
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result, multi, idx = 0, 0, -1

        while idx >= len(columnTitle) * -1:
            char = columnTitle[idx]
            result += (ord(char) - 64) * 26 ** multi
            multi += 1
            idx -= 1

        return result


# Optimized version – left to right, Horner's method
class SolutionClean:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            digit = ord(char) - 64
            result = result * 26 + digit

        return result
