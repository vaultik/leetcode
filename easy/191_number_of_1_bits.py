# 191. Number of 1 Bits
# Difficulty: Easy
# https://leetcode.com/problems/number-of-1-bits/
# Time: O(1) | Space: O(1)


# My solution – check last bit, right shift
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n > 0:
            counter += n & 1
            n >>= 1

        return counter


# Optimized version – Brian Kernighan's algorithm, clears lowest set bit each step
class SolutionKernighan:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n > 0:
            n = n & (n - 1)
            counter += 1

        return counter


# Pythonic version – built-in
class SolutionBuiltin:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
