# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 044 -- Trapping Rain Water
# Category   : Two Pointers
# Difficulty : Hard
# Study Plan : Day 22
# =============================================================
#
# QUESTION:
#   Given heights, compute how much water can be trapped after raining.
#
#   Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
# =============================================================

trap <- function(h) {
    l <- 1; r <- length(h); lm <- 0; rm <- 0; ans <- 0
    while (l<r) {
        if (h[l] < h[r]) { lm <- max(lm,h[l]); ans <- ans + lm - h[l]; l <- l+1 }
        else { rm <- max(rm,h[r]); ans <- ans + rm - h[r]; r <- r-1 }
    }
    ans
}
print(trap(c(0,1,0,2,1,0,1,3,2,1,2,1)))
