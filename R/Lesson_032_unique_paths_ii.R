# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 032 -- Unique Paths II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 16
# =============================================================
#
# QUESTION:
#   You are given an m x n integer array obstacleGrid. There is a robot
#   at the top-left. It moves right or down. An obstacle is marked as 1; an
#   empty space as 0. Return the number of possible unique paths to the
#   bottom-right corner.
#
#   Example:
#     Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2
# =============================================================

uniquePathsWithObstacles <- function(g) {
    R <- nrow(g); C <- ncol(g)
    if (g[1,1] == 1) return(0)
    dp <- integer(C); dp[1] <- 1
    for (r in 1:R) {
        if (g[r,1] == 1) dp[1] <- 0
        if (C > 1) for (c in 2:C) dp[c] <- if (g[r,c] == 1) 0 else dp[c] + dp[c-1]
    }
    dp[C]
}
print(uniquePathsWithObstacles(matrix(c(0,0,0, 0,1,0, 0,0,0), nrow=3, byrow=TRUE)))
