# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 104 -- Non Overlapping Intervals
# Category   : Intervals
# Difficulty : Medium
# Study Plan : Day 52
# =============================================================
#
# QUESTION:
#   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
# =============================================================

eraseOverlapIntervals <- function(intervals){
  intervals <- intervals[order(sapply(intervals, function(x) x[2]))]
  end <- -Inf; rm <- 0
  for (x in intervals){ if (x[1] >= end) end <- x[2] else rm <- rm + 1 }
  rm
}
print(eraseOverlapIntervals(list(c(1,2),c(2,3),c(3,4),c(1,3))))
