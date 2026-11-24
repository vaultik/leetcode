# 38. Count and Say
# Difficulty: Medium
# https://leetcode.com/problems/count-and-say/
# Time: O(n * m) | Space: O(m)
from itertools import groupby


# My solution – manual character counting
class Solution:
    def countAndSay(self, n: int) -> str:
        def encoder(s: str) -> str:
            count = 1
            temp = ''

            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    temp += f'{count}{s[i]}'
                    count = 1

            temp += f'{count}{s[-1]}'
            return temp

        result = '1'

        for _ in range(n - 1):
            result = encoder(result)

        return result


# Optimized version – groupby
class SolutionGroupby:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for _ in range(n - 1):
            chunks = []
            for digit, group in groupby(result):
                count = sum(1 for _ in group)
                chunks.append(f'{count}{digit}')
            result = ''.join(chunks)

        return result
