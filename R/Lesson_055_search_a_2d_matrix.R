# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 055 -- Search a 2D Matrix
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 27
# =============================================================
#
# QUESTION:
#   Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
#   search for target.
#
#   Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
# =============================================================

searchMatrix <- function(m, target) {
    if (length(m)==0) return(FALSE)
    rows <- nrow(m); cols <- ncol(m)
    l <- 0; r <- rows*cols - 1
    while (l <= r) {
        mid <- (l+r) %/% 2
        rr <- mid %/% cols + 1; cc <- mid %% cols + 1
        v <- m[rr, cc]
        if (v == target) return(TRUE)
        if (v < target) l <- mid+1 else r <- mid-1
    }
    FALSE
}
m <- matrix(c(1,3,5,7,10,11,16,20,23,30,34,60), nrow=3, byrow=TRUE)
print(searchMatrix(m, 3))
print(searchMatrix(m, 13))
