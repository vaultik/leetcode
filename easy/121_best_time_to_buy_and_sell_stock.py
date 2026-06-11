# 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time: O(n) | Space: O(1)
from typing import List


# My solution – Runtime 21ms, Beats 94.39%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        min_price = 99999
        max_profit = 0

        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = price - min_price if price - min_price > max_profit else max_profit

        return max_profit


# Cleaner version – uses built-in min/max
class SolutionClean:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
