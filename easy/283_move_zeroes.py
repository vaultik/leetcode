# 283. Move Zeroes
# Difficulty: Easy
# https://leetcode.com/problems/move-zeroes/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – two pointers, swap non-zero to front
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# Optimized version – overwrite non-zero, fill rest with 0
class SolutionFill:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        for i in range(left, len(nums)):
            nums[i] = 0
