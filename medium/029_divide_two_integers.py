# 29. Divide Two Integers
# Difficulty: Medium
# https://leetcode.com/problems/divide-two-integers/
# Time: O(log²n) | Space: O(1)


# My solution – bit shifting with sign handling
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == 1:
            return -2147483648

        sign_dividend = 1 if dividend >= 0 else -1
        sign_divisor = 1 if divisor >= 0 else -1
        count = 0
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            temp_divisor, temp_count = divisor, 1

            while dividend >= temp_divisor:
                count += temp_count
                dividend -= temp_divisor
                temp_divisor <<= 1
                temp_count <<= 1

        count = count if count < 2147483647 else 2147483647

        if sign_divisor == sign_dividend:
            return count if count < 2147483647 else 2147483647
        else:
            return -count if count < 2147483648 else -2147483648


# Optimized version – cleaner sign + edge case handling
class SolutionClean:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_positive = (dividend >= 0) == (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0

        while dividend >= divisor:
            temp_divisor, temp_count = divisor, 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_count <<= 1

            dividend -= temp_divisor
            count += temp_count

        return count if is_positive else -count
