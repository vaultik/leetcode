# 174. Dungeon Game
# Difficulty: Hard
# https://leetcode.com/problems/dungeon-game/
# Time: O(m*n) | Space: O(m*n)
from typing import List


# My solution – bottom-up DP with full matrix (solved with AI hints)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_x, len_y = len(dungeon[0]), len(dungeon)
        matrix = [[float('inf')] * len_x for _ in range(len_y)]
        m, n = len_y - 1, len_x - 1

        matrix[m][n] = max(1, 1 - dungeon[m][n])

        for step in range(n - 1, -1, -1):
            matrix[m][step] = max(1, matrix[m][step + 1] - dungeon[m][step])

        for step in range(m - 1, -1, -1):
            matrix[step][n] = max(1, matrix[step + 1][n] - dungeon[step][n])

        for row in range(m - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                next_step = min(matrix[row][column + 1], matrix[row + 1][column])
                matrix[row][column] = max(1, next_step - dungeon[row][column])

        return matrix[0][0]


# Optimized version – 1D DP array, O(n) space
# Time: O(m*n) | Space: O(n)
class SolutionOptimal:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_x, len_y = len(dungeon[0]), len(dungeon)
        dp = [float('inf')] * (len_x + 1)
        dp[len_x - 1] = 1

        for r in range(len_y - 1, -1, -1):
            for c in range(len_x - 1, -1, -1):
                next_step = min(dp[c], dp[c + 1])
                dp[c] = max(1, next_step - dungeon[r][c])

        return dp[0]
