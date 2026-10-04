# 7. Reverse Integer
# Difficulty: Medium
# https://leetcode.com/problems/reverse-integer/
# Time: O(log n) | Space: O(1)


# My solution – string reversal with sign handling
class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x

        minus = False if x >= 0 else True
        x = abs(x)
        result = ''

        for n in str(x)[::-1]:
            if not result and n == '0':
                continue
            result += n

        result = int('-' + result) if minus else int(result)
        return result if -2**31 <= result <= 2**31 - 1 else 0


# Optimized version – math with divmod, no string conversion
class SolutionMath:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x > 0:
            x, remainder = divmod(x, 10)
            result = result * 10 + remainder

            if sign * result < INT_MIN or sign * result > INT_MAX:
                return 0

        return sign * result
