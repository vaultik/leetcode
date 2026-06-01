# 744. Find Smallest Letter Greater Than Target
# Difficulty: Easy
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Time: O(n) | Space: O(1)

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        for let in letters:
            if let > target:
                return let
        return ''
