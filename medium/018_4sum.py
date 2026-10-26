# 18. 4Sum
# Difficulty: Medium
# https://leetcode.com/problems/4sum/
# Time: O(n³) | Space: O(n)
from typing import List


# My solution – sort + two nested loops + two pointers
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <= 4:
            return [nums] if len(nums) == 4 and sum(nums) == target else []

        sort_nums = sorted(nums)
        n = len(sort_nums)
        result = []

        for idx1 in range(n - 3):
            if idx1 > 0 and sort_nums[idx1] == sort_nums[idx1 - 1]:
                continue

            for idx2 in range(idx1 + 1, n - 2):
                if idx2 > idx1 + 1 and sort_nums[idx2] == sort_nums[idx2 - 1]:
                    continue

                left = idx2 + 1
                right = n - 1

                while left < right:
                    current_sum = sort_nums[idx1] + sort_nums[idx2] + sort_nums[left] + sort_nums[right]

                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([sort_nums[idx1], sort_nums[idx2], sort_nums[left], sort_nums[right]])
                        left += 1
                        right -= 1
                        while left < right and sort_nums[left] == sort_nums[left - 1]:
                            left += 1
                        while left < right and sort_nums[right] == sort_nums[right + 1]:
                            right -= 1

        return result


# Optimized version – pruning with min/max bounds
class SolutionPruned:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        sort_nums = sorted(nums)
        result = []

        for idx1 in range(n - 3):
            if idx1 > 0 and sort_nums[idx1] == sort_nums[idx1 - 1]:
                continue
            if sort_nums[idx1] + sort_nums[idx1 + 1] + sort_nums[idx1 + 2] + sort_nums[idx1 + 3] > target:
                break
            if sort_nums[idx1] + sort_nums[n - 3] + sort_nums[n - 2] + sort_nums[n - 1] < target:
                continue

            for idx2 in range(idx1 + 1, n - 2):
                if idx2 > idx1 + 1 and sort_nums[idx2] == sort_nums[idx2 - 1]:
                    continue
                if sort_nums[idx1] + sort_nums[idx2] + sort_nums[idx2 + 1] + sort_nums[idx2 + 2] > target:
                    break
                if sort_nums[idx1] + sort_nums[idx2] + sort_nums[n - 2] + sort_nums[n - 1] < target:
                    continue

                left = idx2 + 1
                right = n - 1

                while left < right:
                    current_sum = sort_nums[idx1] + sort_nums[idx2] + sort_nums[left] + sort_nums[right]

                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([sort_nums[idx1], sort_nums[idx2], sort_nums[left], sort_nums[right]])
                        left += 1
                        right -= 1
                        while left < right and sort_nums[left] == sort_nums[left - 1]:
                            left += 1
                        while left < right and sort_nums[right] == sort_nums[right + 1]:
                            right -= 1

        return result
