# 3300. Minimum Element After Replacement With Digit Sum
# Difficulty: Easy
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

from typing import List


# Approach 1: Explicit loop
# Time: O(n * k) | Space: O(n)
class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            plus = 0
            for digit in str(num):
                plus += int(digit)
            result.append(plus)
        return min(result)


# Approach 2: One-liner with generator
# Time: O(n * k) | Space: O(1)
class Solution2:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(d) for d in str(num)) for num in nums)
