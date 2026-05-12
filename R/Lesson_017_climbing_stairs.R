# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 017 -- Climbing Stairs
# Category   : 1-D Dynamic Programming
# Difficulty : Easy
# Study Plan : Day 9
# =============================================================
#
# QUESTION:
#   You are climbing a staircase. It takes n steps to reach the top. Each
#   time you can climb 1 or 2 steps. In how many distinct ways can you climb
#   to the top?
#
#   Example:
#     Input : n = 2  -> 2
#     Input : n = 3  -> 3
# =============================================================

climbStairs <- function(n) {
    a <- 1; b <- 1
    for (i in seq_len(n)) { t <- a + b; a <- b; b <- t }
    a
}
print(c(climbStairs(2), climbStairs(3), climbStairs(5)))
