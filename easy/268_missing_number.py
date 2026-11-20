# 268. Missing Number
# Difficulty: Easy
# https://leetcode.com/problems/missing-number/
# Time: O(n log n) | Space: O(1)
from typing import List


# My solution – sort, check gaps
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)

        if sort_nums[0] != 0:
            return 0

        for i in range(1, len(sort_nums)):
            if sort_nums[i] - sort_nums[i - 1] > 1:
                return sort_nums[i] - 1

        return sort_nums[-1] + 1


# Optimized version – Gauss formula, O(n) time O(1) space
class SolutionMath:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


# Bit manipulation – XOR
class SolutionXOR:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
