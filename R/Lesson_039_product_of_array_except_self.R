# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 039 -- Product of Array Except Self
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 19
# =============================================================
#
# QUESTION:
#   Given nums, return an array where answer[i] is the product of all elements
#   except nums[i]. Must run in O(n) without division.
#
#   Example: [1,2,3,4] -> [24,12,8,6]
# =============================================================

productExceptSelf <- function(nums) {
    n <- length(nums); r <- rep(1L, n); left <- 1
    for (i in seq_len(n)) { r[i] <- left; left <- left * nums[i] }
    right <- 1
    for (i in n:1) { r[i] <- r[i] * right; right <- right * nums[i] }
    r
}
print(productExceptSelf(c(1,2,3,4)))
