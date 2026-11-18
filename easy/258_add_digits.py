# 258. Add Digits
# Difficulty: Easy
# https://leetcode.com/problems/add-digits/
# Time: O(n) | Space: O(1)


# My solution – loop until single digit
class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 < 1:
            return num

        def counter(number):
            count = 0
            while number:
                count += number % 10
                number //= 10
            return count

        while num // 10 > 0:
            num = counter(num)

        return num


# Optimized version – digital root formula, O(1)
class SolutionMath:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
