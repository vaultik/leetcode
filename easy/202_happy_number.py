# 202. Happy Number
# Difficulty: Easy
# https://leetcode.com/problems/happy-number/
# Time: O(log n) | Space: O(log n)


# My solution – seen set to detect cycle
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            result = 0

            while n:
                n, digit = divmod(n, 10)
                result += digit ** 2

            if result == 1:
                return True

            if result in seen:
                return False
            else:
                seen.add(result)

            n = result


# Optimized version – Floyd's cycle detection, O(1) space
# Time: O(log n) | Space: O(1)
class SolutionFloyd:
    def get_next(self, number: int) -> int:
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)

        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return fast == 1
