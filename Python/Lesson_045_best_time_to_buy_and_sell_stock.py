# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 045 -- Best Time to Buy and Sell Stock
# Category   : Sliding Window
# Difficulty : Easy
# Study Plan : Day 22
# =============================================================
#
# QUESTION:
#   Given prices, return the maximum profit from a single buy/sell.
#
#   Example: [7,1,5,3,6,4] -> 5
# =============================================================

class Solution:
    def maxProfit(self, prices):
        lo = float("inf"); best = 0
        for p in prices:
            if p < lo: lo = p
            elif p - lo > best: best = p - lo
        return best

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
