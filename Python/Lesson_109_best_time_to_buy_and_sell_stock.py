# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 109 -- Best Time to Buy And Sell Stock
# Category   : Sliding Window
# Difficulty : Easy
# Study Plan : Day 55
# =============================================================
#
# QUESTION:
#   Given an array of stock prices where prices[i] is on day i, return the maximum profit from a single buy/sell. Return 0 if none.
# =============================================================

class Solution:
    def maxProfit(self, prices):
        lo=float('inf'); best=0
        for p in prices:
            lo=min(lo,p); best=max(best, p-lo)
        return best

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
