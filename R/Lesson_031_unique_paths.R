# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 031 -- Unique Paths
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 16
# =============================================================
#
# QUESTION:
#   A robot is on an m x n grid at the top-left. It can only move right or
#   down. How many possible unique paths are there to reach the bottom-right?
#
#   Example:
#     Input : m=3, n=7  Output: 28
#     Input : m=3, n=2  Output: 3
# =============================================================

uniquePaths <- function(m, n) {
    dp <- rep(1, n)
    if (m > 1) for (i in 2:m) for (j in 2:n) dp[j] <- dp[j] + dp[j-1]
    dp[n]
}
print(c(uniquePaths(3,7), uniquePaths(3,2)))
