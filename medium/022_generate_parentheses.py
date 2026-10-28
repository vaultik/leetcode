# 22. Generate Parentheses
# Difficulty: Medium
# https://leetcode.com/problems/generate-parentheses/
# Time: O(4^n / √n) | Space: O(n)
from typing import List


# My solution – backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recursion(current_str: str, left: int, right: int) -> None:
            if left == n and right == n:
                result.append(current_str)
                return
            if left < n:
                recursion(current_str + '(', left + 1, right)
            if left > right:
                recursion(current_str + ')', left, right + 1)

        recursion('', 0, 0)
        return result


# Optimized version – DP, build from smaller valid combinations
class SolutionDP:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']

        for num_pairs in range(1, n + 1):
            for i in range(num_pairs):
                j = num_pairs - 1 - i
                for left_part in dp[i]:
                    for right_part in dp[j]:
                        dp[num_pairs].append(f'({left_part}){right_part}')

        return dp[n]
