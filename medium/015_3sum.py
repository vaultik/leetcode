# 15. 3Sum
# Difficulty: Medium
# https://leetcode.com/problems/3sum/
# Time: O(n²) | Space: O(n)
from typing import List


# My solution – sort + two pointers + skip duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []

        nums_sort = sorted(nums)
        result = []

        for i in range(len(nums_sort) - 2):
            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue

            left = i + 1
            right = len(nums_sort) - 1

            while left < right:
                current_sum = nums_sort[i] + nums_sort[left] + nums_sort[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums_sort[i], nums_sort[left], nums_sort[right]])
                    right -= 1
                    left += 1

                    while left < right and nums_sort[left] == nums_sort[left - 1]:
                        left += 1
                    while left < right and nums_sort[right] == nums_sort[right + 1]:
                        right -= 1

        return result


# Optimized version – early exit pruning
class SolutionPruned:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        n = len(nums_sort)
        result = []

        if n < 3:
            return []
        if nums_sort[0] + nums_sort[1] + nums_sort[2] > 0:
            return []
        if nums_sort[-1] + nums_sort[-2] + nums_sort[-3] < 0:
            return []

        for i in range(n - 2):
            curr = nums_sort[i]

            if curr > 0:
                break
            if i > 0 and curr == nums_sort[i - 1]:
                continue
            if curr + nums_sort[i + 1] + nums_sort[i + 2] > 0:
                break
            if curr + nums_sort[-1] + nums_sort[-2] < 0:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                l_val = nums_sort[left]
                r_val = nums_sort[right]
                current_sum = curr + l_val + r_val

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([curr, l_val, r_val])
                    while left < right and nums_sort[left] == l_val:
                        left += 1
                    while left < right and nums_sort[right] == r_val:
                        right -= 1

        return result
