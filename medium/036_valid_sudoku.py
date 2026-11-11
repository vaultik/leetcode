# 36. Valid Sudoku
# Difficulty: Medium
# https://leetcode.com/problems/valid-sudoku/
# Time: O(1) | Space: O(1)
from typing import List


# My solution – single set with string keys
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                point = (
                    f'{value} in row {row}',
                    f'{value} in col {col}',
                    f'{value} in matrix {row // 3}-{col // 3}'
                )
                for p in point:
                    if p in seen:
                        return False
                    seen.add(p)

        return True


# Optimized version – 9 sets per row/col/box, faster lookup
class SolutionSets:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_idx = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
