# 58. Length of Last Word
# Difficulty: Easy
# https://leetcode.com/problems/length-of-last-word/
# Time: O(n) | Space: O(1)


# My solution – rstrip + rfind
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.rstrip()
        return len(text) - text.rfind(' ') - 1


# Pythonic version – split
class SolutionSplit:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# Optimized version – two pointers from end
# Time: O(n) | Space: O(1)
class SolutionPointers:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length