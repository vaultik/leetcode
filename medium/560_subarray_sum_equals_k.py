# 560. Subarray Sum Equals K
# Difficulty: Medium
# https://leetcode.com/problems/subarray-sum-equals-k/
# Time: O(n) | Space: O(n)
from typing import List
from collections import defaultdict


# My solution – prefix sum + hash map
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        current_sum, result = 0, 0
        sums_count = {0: 1}

        for num in nums:
            current_sum += num
            if (current_sum - k) in sums_count:
                result += sums_count[current_sum - k]
            if current_sum in sums_count:
                sums_count[current_sum] += 1
            else:
                sums_count[current_sum] = 1

        return result


# Optimized version – defaultdict, cleaner code
class SolutionClean:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_count = defaultdict(int)
        sums_count[0] = 1

        current_sum, result = 0, 0

        for num in nums:
            current_sum += num
            result += sums_count[current_sum - k]
            sums_count[current_sum] += 1

        return result
