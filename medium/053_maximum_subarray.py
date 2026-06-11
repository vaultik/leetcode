# 53. Maximum Subarray
# Difficulty: Medium
# https://leetcode.com/problems/maximum-subarray/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – Kadane's algorithm, O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for num in nums:
            if current_sum > 0:
                current_sum += num
            else:
                current_sum = num

            max_sum = current_sum if current_sum > max_sum else max_sum

        return max_sum
