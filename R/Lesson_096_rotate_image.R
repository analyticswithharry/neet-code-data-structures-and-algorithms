# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 096 -- Rotate Image
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 48
# =============================================================
#
# QUESTION:
#   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
# =============================================================

rotate <- function(m){
  n <- nrow(m); res <- matrix(0, n, n)
  for (i in 1:n) for (j in 1:n) res[i, n-j+1] <- m[j, i]
  res
}
print(rotate(matrix(1:9, 3, 3, byrow=TRUE)))
