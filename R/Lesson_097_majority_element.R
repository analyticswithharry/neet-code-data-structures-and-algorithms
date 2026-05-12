# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 097 -- Majority Element
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 49
# =============================================================
#
# QUESTION:
#   Given an array of size n, return the element that appears more than n/2 times.
# =============================================================

majorityElement <- function(nums){
  cand <- 0; cnt <- 0
  for (n in nums){ if (cnt==0) cand <- n; cnt <- cnt + ifelse(n==cand, 1, -1) }
  cand
}
print(majorityElement(c(3,2,3)))
print(majorityElement(c(2,2,1,1,1,2,2)))
