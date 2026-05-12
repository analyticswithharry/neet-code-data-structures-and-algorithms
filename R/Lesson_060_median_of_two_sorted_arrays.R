# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 060 -- Median of Two Sorted Arrays
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 30
# =============================================================
#
# QUESTION:
#   Given two sorted arrays nums1 and nums2, return the median of the
#   combined sorted array. Run in O(log(min(m,n))).
#
#   Example: [1,3], [2] -> 2.0
# =============================================================

findMedianSortedArrays <- function(a, b) {
    c <- sort(c(a, b)); n <- length(c)
    if (n %% 2 == 1) c[(n+1) %/% 2]
    else (c[n/2] + c[n/2 + 1]) / 2
}
print(findMedianSortedArrays(c(1,3), c(2)))
print(findMedianSortedArrays(c(1,2), c(3,4)))
