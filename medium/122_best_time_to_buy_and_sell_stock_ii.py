# 122. Best Time to Buy and Sell Stock II
# Difficulty: Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – greedy, O(n) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        result = 0

        for price in prices:
            if price > prev:
                result += price - prev
            prev = price

        return result


# Cleaner version – one-liner generator
class SolutionClean:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))
