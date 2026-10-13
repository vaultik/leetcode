# 11. Container With Most Water
# Difficulty: Medium
# https://leetcode.com/problems/container-with-most-water/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – two pointers, move shorter side
class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = 0
        y = len(height) - 1
        result = 0

        while x < y:
            minimum = height[x] if height[x] < height[y] else height[y]
            result = minimum * (y - x) if minimum * (y - x) > result else result

            if minimum == height[x]:
                x += 1
            else:
                y -= 1

        return result


# Optimized version – skip duplicates with inner while loop
class SolutionSkipDupes:
    def maxArea(self, height: List[int]) -> int:
        x = 0
        y = len(height) - 1
        result = 0

        while x < y:
            hx = height[x]
            hy = height[y]

            if hx < hy:
                area = hx * (y - x)
                result = area if area > result else result
                while x < y and height[x] <= hx:
                    x += 1
            else:
                area = hy * (y - x)
                result = area if area > result else result
                while x < y and height[y] <= hy:
                    y -= 1

        return result
