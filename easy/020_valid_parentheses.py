# 20. Valid Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/
# Time: O(n) | Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return len(stack) == 0
