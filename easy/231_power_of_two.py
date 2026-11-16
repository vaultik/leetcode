# 231. Power of Two
# Difficulty: Easy
# https://leetcode.com/problems/power-of-two/
# Time: O(1) | Space: O(1)


# My solution – loop with modulo check
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2**30 % n == 0


# Optimized version – bit trick: power of two has exactly one set bit
class SolutionBit:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


# Pythonic version – built-in bit_count
class SolutionBuiltin:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1
