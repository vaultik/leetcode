# 1. Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lasts = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in lasts:
                return [lasts[find], i]
            lasts[num] = i
        return []
