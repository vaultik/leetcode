# 70. Climbing Stairs
# Difficulty: Easy
# https://leetcode.com/problems/climbing-stairs/
# Time: O(n) | Space: O(1)

# My solution – two variables, O(n) time, O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 2

        for _ in range(3, n):
            a, b = b, a + b

        return a + b


# Math solution – Binet's formula, O(1) time and space (float precision risk on large n)
import math

class SolutionBinet:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        return round(phi ** (n + 1) / sqrt5)
