# 40. Combination Sum II
# Difficulty: Medium
# https://leetcode.com/problems/combination-sum-ii/
# Time: O(2^n) | Space: O(n)
from typing import List


# My solution – backtracking, skip duplicates (solved with AI hints)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def recursion(remain, comb, idx):
            if remain == 0:
                result.append(comb)
                return
            elif remain < 0:
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > remain:
                    break
                if i != idx and candidates[i] == candidates[i - 1]:
                    continue
                recursion(remain - candidates[i], comb + [candidates[i]], i + 1)

        recursion(target, [], 0)
        return result


# Optimized version – in-place comb, same skip logic
class SolutionOptimal:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        comb = []

        def backtrack(remain, start):
            if remain == 0:
                result.append(comb[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(remain - candidates[i], i + 1)
                comb.pop()

        backtrack(target, 0)
        return result
