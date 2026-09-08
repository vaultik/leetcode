# 35. Search Insert Position
# Difficulty: Easy
# https://leetcode.com/problems/search-insert-position/
# Time: O(n) | Space: O(1)
from typing import List
import bisect


# My solution – linear scan
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        if nums[-1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i


# Optimized version – binary search
# Time: O(log n) | Space: O(1)
class SolutionBinary:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        if nums[-1] < target:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left


# Pythonic version – bisect
class SolutionBisect:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)