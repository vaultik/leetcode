# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Time: O(n) | Space: O(n)
from typing import List
from collections import Counter


# My solution – dict counter with early exit
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(set(nums)) == 1:
            return nums[0]

        result_length = len(nums) // 2
        count = {}

        for i, num in enumerate(nums):
            count[num] = count[num] + 1 if num in count else 1
            if i > result_length and count[num] > result_length:
                return num

        return max(count, key=count.get)


# Optimized version – Boyer-Moore voting algorithm, O(1) space
# Time: O(n) | Space: O(1)
class SolutionBoyerMoore:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Pythonic version – Counter
class SolutionCounter:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
