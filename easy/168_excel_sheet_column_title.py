# 168. Excel Sheet Column Title
# Difficulty: Easy
# https://leetcode.com/problems/excel-sheet-column-title/
# Time: O(log n) | Space: O(log n)


# My solution – chr lookup with alphabet list
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        alphabet = [chr(x) for x in range(65, 91)]

        while columnNumber > 0:
            columnNumber -= 1
            idx = columnNumber % 26
            result = alphabet[idx] + result
            columnNumber = columnNumber // 26

        return result


# Optimized version – divmod, list append + reverse
class SolutionClean:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            result.append(chr(65 + remainder))

        return ''.join(reversed(result))
