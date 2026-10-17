# 16. 3Sum Closest
# Difficulty: Medium
# https://leetcode.com/problems/3sum-closest/
# Time: O(n²) | Space: O(n)
from typing import List


# My solution – sort + two pointers + track closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums_sort = sorted(nums)
        result = nums_sort[0] + nums_sort[1] + nums_sort[2]

        for i in range(len(nums_sort) - 2):
            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue

            left = i + 1
            right = len(nums_sort) - 1

            while left < right:
                current_sum = nums_sort[i] + nums_sort[left] + nums_sort[right]

                if current_sum == target:
                    return current_sum

                result = current_sum if abs(target - current_sum) < abs(target - result) else result

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


# Optimized version – min/max pruning per outer iteration
class SolutionPruned:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sort = sorted(nums)
        n = len(nums_sort)
        result = nums_sort[0] + nums_sort[1] + nums_sort[2]

        for i in range(n - 2):
            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue

            left = i + 1
            right = n - 1

            min_sum = nums_sort[i] + nums_sort[left] + nums_sort[left + 1]
            if min_sum > target:
                if abs(min_sum - target) < abs(result - target):
                    result = min_sum
                continue

            max_sum = nums_sort[i] + nums_sort[right - 1] + nums_sort[right]
            if max_sum < target:
                if abs(max_sum - target) < abs(result - target):
                    result = max_sum
                continue

            while left < right:
                current_sum = nums_sort[i] + nums_sort[left] + nums_sort[right]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(result - target):
                    result = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
