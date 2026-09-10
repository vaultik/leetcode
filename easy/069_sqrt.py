# 69. Sqrt(x)
# Difficulty: Easy
# https://leetcode.com/problems/sqrtx/
# Time: O(log n) | Space: O(1)


# My solution – binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if x == mid * mid:
                return mid
            if x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1
        return right


# Optimized version – Newton's method
class SolutionNewton:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        guess = x // 2

        while guess * guess > x:
            guess = (guess + x // guess) // 2

        return guess