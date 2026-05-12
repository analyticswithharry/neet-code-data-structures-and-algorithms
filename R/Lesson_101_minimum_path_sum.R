# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 101 -- Minimum Path Sum
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 51
# =============================================================
#
# QUESTION:
#   Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).
# =============================================================

minPathSum <- function(g){
  R <- nrow(g); C <- ncol(g)
  for (i in 1:R) for (j in 1:C){
    if (i==1 && j==1) next
    if (i==1) g[i,j] <- g[i,j] + g[i,j-1]
    else if (j==1) g[i,j] <- g[i,j] + g[i-1,j]
    else g[i,j] <- g[i,j] + min(g[i-1,j], g[i,j-1])
  }
  g[R,C]
}
print(minPathSum(matrix(c(1,3,1,1,5,1,4,2,1), 3, 3, byrow=TRUE)))
