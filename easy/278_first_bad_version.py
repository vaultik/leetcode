# 278. First Bad Version
# Difficulty: Easy
# https://leetcode.com/problems/first-bad-version/
# Time: O(log n) | Space: O(1)
from bisect import bisect_left


# My solution – binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Optimized version – bisect_left with key
class SolutionBisect:
    def firstBadVersion(self, n: int) -> int:
        return bisect_left(range(n + 1), True, 1, n, key=isBadVersion)
