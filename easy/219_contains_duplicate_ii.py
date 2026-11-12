# 219. Contains Duplicate II
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate-ii/
# Time: O(n) | Space: O(n)
from typing import List


# My solution – dict storing last seen index
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for i, num in enumerate(nums):
            if num in seen:
                diff = abs(seen.get(num) - i)
                if diff <= k:
                    return True
            seen[num] = i

        return False


# Optimized version – sliding window set, O(k) space
class SolutionWindow:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])

        return False
