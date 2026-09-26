# 136. Single Number
# Difficulty: Easy
# https://leetcode.com/problems/single-number/
# Time: O(n) | Space: O(n)
from typing import List
from collections import defaultdict


# My solution – set, remove on second occurrence
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = set()

        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)

        return next(iter(result))


# Alternative – dict counter
class SolutionDict:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num] += 1

        return next(key for key, value in my_dict.items() if value == 1)


# Optimized version – XOR, O(1) space
# Time: O(n) | Space: O(1)
class SolutionXOR:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
