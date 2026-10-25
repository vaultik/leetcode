# 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Time: O(4^n) | Space: O(4^n)
from typing import List
from itertools import product


# My solution – iterative build
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ('', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        result = ['']

        for digit in digits:
            temp = []
            for prev in result:
                for char in phone[int(digit)]:
                    temp.append(prev + char)
            result = temp

        return result


# Alternative – itertools.product
class SolutionProduct:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        letters = [phone[d] for d in digits]
        return [''.join(p) for p in product(*letters)]


# Optimized version – backtracking
class SolutionBacktrack:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []

        def backtrack(index: int, current: str) -> None:
            if len(current) == len(digits):
                result.append(current)
                return
            for letter in phone[digits[index]]:
                backtrack(index + 1, current + letter)

        backtrack(0, '')
        return result
