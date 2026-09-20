# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: O(n) | Space: O(n)


# My solution – sliding window with set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        check = set()

        while right < len(s):
            while s[right] in check:
                check.remove(s[left])
                left += 1

            check.add(s[right])
            max_length = len(check) if len(check) > max_length else max_length
            right += 1

        return max_length


# Optimized version – sliding window with dict, O(1) jump on duplicate
class SolutionDict:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length

        return max_length
