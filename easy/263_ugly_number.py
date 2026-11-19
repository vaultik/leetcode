# 263. Ugly Number
# Difficulty: Easy
# https://leetcode.com/problems/ugly-number/
# Time: O(log n) | Space: O(1)


# My solution – divide by 2, 3, 5 with if/elif
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False

        return True


# Optimized version – loop over factors, cleaner
class SolutionClean:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1
