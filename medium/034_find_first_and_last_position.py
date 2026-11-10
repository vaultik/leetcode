# 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Time: O(log n) | Space: O(1)
from typing import List
import bisect


# My solution – two binary searches with direction flag
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search(is_left: bool) -> int:
            temp = -1
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    temp = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return temp

        return [binary_search(is_left=True), binary_search(is_left=False)]


# Optimized version – bisect
class SolutionBisect:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        if left < len(nums) and nums[left] == target:
            return [left, right]

        return [-1, -1]
