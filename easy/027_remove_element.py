# 27. Remove Element
# Difficulty: Easy
# https://leetcode.com/problems/remove-element/
# Time: O(n²) | Space: O(1)
from typing import List


# My solution – uses pop()
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0

        while idx < len(nums):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)


# Optimized version – two pointers
# Time: O(n) | Space: O(1)
class SolutionClean:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        i = 0

        while i < k:
            if nums[i] == val:
                nums[i] = nums[k - 1]
                k -= 1
            else:
                i += 1

        return k
