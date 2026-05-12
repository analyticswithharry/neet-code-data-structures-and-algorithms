# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 054 -- Largest Rectangle in Histogram
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 27
# =============================================================
#
# QUESTION:
#   Given heights of bars, find the area of the largest rectangle.
#
#   Example: [2,1,5,6,2,3] -> 10
# =============================================================

largestRectangleArea <- function(h) {
    st_i <- c(); st_v <- c(); best <- 0
    h2 <- c(h, 0)
    for (i in seq_along(h2)) {
        start <- i
        while (length(st_v) > 0 && st_v[length(st_v)] > h2[i]) {
            idx <- st_i[length(st_i)]; ht <- st_v[length(st_v)]
            st_i <- st_i[-length(st_i)]; st_v <- st_v[-length(st_v)]
            best <- max(best, ht*(i-idx))
            start <- idx
        }
        st_i <- c(st_i, start); st_v <- c(st_v, h2[i])
    }
    best
}
print(largestRectangleArea(c(2,1,5,6,2,3)))
