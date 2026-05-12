# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 043 -- Container With Most Water
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 21
# =============================================================
#
# QUESTION:
#   Given heights, find two lines that with the x-axis form a container
#   holding the most water. Return the max area.
#
#   Example: [1,8,6,2,5,4,8,3,7] -> 49
# =============================================================

maxArea <- function(h) {
    i <- 1; j <- length(h); best <- 0
    while (i<j) {
        a <- (j-i)*min(h[i],h[j])
        if (a > best) best <- a
        if (h[i] < h[j]) i <- i+1 else j <- j-1
    }
    best
}
print(maxArea(c(1,8,6,2,5,4,8,3,7)))
