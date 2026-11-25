# 39. Combination Sum
# Difficulty: Medium
# https://leetcode.com/problems/combination-sum/
# Time: O(n^(t/m)) | Space: O(t/m)
from typing import List


# My solution – backtracking (solved with AI hints)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def recursion(remain, comb, idx):
            if remain == 0:
                result.append(comb)
                return
            elif remain < 0:
                return

            for i in range(idx, len(candidates)):
                recursion(remain - candidates[i], comb + [candidates[i]], i)

        recursion(target, [], 0)
        return result


# Optimized version – sort + early break, in-place comb
class SolutionOptimal:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remain: int, current_comb: List[int], start_idx: int):
            if remain == 0:
                result.append(list(current_comb))
                return

            for i in range(start_idx, len(candidates)):
                if candidates[i] > remain:
                    break
                current_comb.append(candidates[i])
                backtrack(remain - candidates[i], current_comb, i)
                current_comb.pop()

        backtrack(target, [], 0)
        return result
