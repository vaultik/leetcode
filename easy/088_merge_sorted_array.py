# 88. Merge Sorted Array
# Difficulty: Easy
# https://leetcode.com/problems/merge-sorted-array/
# Time: O((m+n) log(m+n)) | Space: O(1)
from typing import List


# My solution – slice + sort
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


# Optimized version – three pointers from end
# Time: O(m+n) | Space: O(1)
class SolutionPointers:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1