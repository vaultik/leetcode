# 704. Binary Search
# Difficulty: Easy
# https://leetcode.com/problems/binary-search/
# Time: O(log n) | Space: O(1)
from typing import List


# My solution – classic binary search, O(log n) time, O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Alternative – bisect from standard library (same complexity, written in C)
import bisect


class SolutionBisect:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1
