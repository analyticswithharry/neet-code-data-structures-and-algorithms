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

maxProfit <- function(prices) {
    lo <- Inf; best <- 0
    for (p in prices) {
        if (p < lo) lo <- p
        else if (p - lo > best) best <- p - lo
    }
    best
}
print(maxProfit(c(7,1,5,3,6,4)))
