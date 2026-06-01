# 9. Palindrome Number
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-number/
# Time: O(n) | Space: O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
