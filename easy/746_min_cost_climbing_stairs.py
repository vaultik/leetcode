# 746. Min Cost Climbing Stairs
# Difficulty: Easy
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


# Solution 1 — DP array (O(n) time | O(n) space)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


# Solution 2 — two variables (O(n) time | O(1) space)
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in range(2, len(cost) + 1):
            prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        return prev1
