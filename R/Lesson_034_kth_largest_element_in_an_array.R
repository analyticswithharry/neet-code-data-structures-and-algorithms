# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 034 -- Kth Largest Element In An Array
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 17
# =============================================================
#
# QUESTION:
#   Given an integer array nums and an integer k, return the kth largest
#   element in the array (the kth largest in sorted order, not the kth
#   distinct element).
#
#   Example:
#     Input : [3,2,1,5,6,4], k=2   Output: 5
# =============================================================

findKthLargest <- function(nums, k) sort(nums, decreasing=TRUE)[k]
print(findKthLargest(c(3,2,1,5,6,4), 2))
