# 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time: O(n log n) | Space: O(n)
from typing import List


# My solution – uses set
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums[:] = sorted(set(nums))

        return len(nums)


# Optimized version – two pointers
# Time: O(n) | Space: O(1)
class SolutionClean:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[k] = nums[idx]
                k += 1

        return k
