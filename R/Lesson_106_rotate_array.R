# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 106 -- Rotate Array
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 53
# =============================================================
#
# QUESTION:
#   Rotate the array to the right by k steps in-place.
# =============================================================

rotateArr <- function(nums, k){
  n <- length(nums); k <- k %% n
  c(nums[(n-k+1):n], nums[1:(n-k)])
}
print(rotateArr(c(1,2,3,4,5,6,7), 3))
