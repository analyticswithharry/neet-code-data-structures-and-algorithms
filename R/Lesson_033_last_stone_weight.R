# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 033 -- Last Stone Weight
# Category   : Heap Priority Queue
# Difficulty : Easy
# Study Plan : Day 17
# =============================================================
#
# QUESTION:
#   You are given an array of stones. On each turn pick the two heaviest
#   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
#   and y becomes y - x. Return the weight of the last remaining stone (or 0).
#
#   Example:
#     Input : [2,7,4,1,8,1]   Output: 1
# =============================================================

lastStoneWeight <- function(stones) {
    s <- stones
    while (length(s) > 1) {
        s <- sort(s)
        y <- s[length(s)]; x <- s[length(s)-1]
        s <- s[-c(length(s), length(s)-1)]
        if (y != x) s <- c(s, y - x)
    }
    if (length(s) == 0) 0L else s[1]
}
print(lastStoneWeight(c(2,7,4,1,8,1)))
