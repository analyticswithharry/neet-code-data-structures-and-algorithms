# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 103 -- Merge Intervals
# Category   : Intervals
# Difficulty : Medium
# Study Plan : Day 52
# =============================================================
#
# QUESTION:
#   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
# =============================================================

mergeIntervals <- function(intervals){
  intervals <- intervals[order(sapply(intervals, function(x) x[1]))]
  res <- list()
  for (x in intervals){
    n <- length(res)
    if (n > 0 && x[1] <= res[[n]][2]) res[[n]][2] <- max(res[[n]][2], x[2])
    else res[[length(res)+1]] <- x
  }
  res
}
print(mergeIntervals(list(c(1,3),c(2,6),c(8,10),c(15,18))))
