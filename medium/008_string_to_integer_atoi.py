# 8. String to Integer (atoi)
# Difficulty: Medium
# https://leetcode.com/problems/string-to-integer-atoi/
# Time: O(n) | Space: O(1)


# My solution – strip, sign, digit loop
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        MAX_NUM, MIN_NUM = 2**31 - 1, -2**31
        result, sign = 0, 1

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for char in s:
            if char.isdigit():
                result = result * 10 + (ord(char) - ord('0'))
            else:
                break

        result *= sign
        return max(MIN_NUM, min(MAX_NUM, result))


# Optimized version – index pointer, early clamp on overflow
class SolutionClean:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - 48
            result = result * 10 + digit

            if sign * result >= INT_MAX:
                return INT_MAX
            if sign * result <= INT_MIN:
                return INT_MIN

            i += 1

        return sign * result
