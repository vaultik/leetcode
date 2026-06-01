# 14. Longest Common Prefix
# Difficulty: Easy
# https://leetcode.com/problems/longest-common-prefix/
# Time: O(n * m) | Space: O(1)

from typing import List


# Solution 1 — first attempt
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_nums = min(len(s) for s in strs)
        result = ''
        for _ in range(max_nums):
            for s in strs:
                k = strs[0][:max_nums]
                if k == s[:max_nums]:
                    result = k
                else:
                    result = result[:-1]
                    max_nums -= 1
        return result


# Solution 2 — optimized (shrink prefix)
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ''
        return prefix
