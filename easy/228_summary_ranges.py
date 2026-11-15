# 228. Summary Ranges
# Difficulty: Easy
# https://leetcode.com/problems/summary-ranges/
# Time: O(n) | Space: O(n)
from typing import List
from itertools import groupby


# My solution – two pointers a, b
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        a, b = 0, 1
        n = len(nums) - 1
        result = []

        while b <= n:
            if nums[b] - nums[b - 1] != 1:
                if a == b - 1:
                    result.append(f'{nums[a]}')
                else:
                    result.append(f'{nums[a]}->{nums[b - 1]}')
                a = b
            b += 1

        if a == n:
            result.append(f'{nums[a]}')
        else:
            result.append(f'{nums[a]}->{nums[n]}')

        return result


# Optimized version – walk to end of each range
class SolutionClean:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            while i + 1 < n and nums[i + 1] - nums[i] == 1:
                i += 1

            if start == nums[i]:
                result.append(f'{start}')
            else:
                result.append(f'{start}->{nums[i]}')

            i += 1

        return result


# Pythonic version – groupby enumerate trick
class SolutionGroupby:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        for _, group in groupby(enumerate(nums), lambda x: x[1] - x[0]):
            group_list = list(group)
            start = group_list[0][1]
            end = group_list[-1][1]
            result.append(f'{start}' if start == end else f'{start}->{end}')

        return result
