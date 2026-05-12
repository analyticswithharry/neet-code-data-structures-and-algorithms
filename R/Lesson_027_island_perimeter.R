# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 027 -- Island Perimeter
# Category   : Graphs
# Difficulty : Easy
# Study Plan : Day 14
# =============================================================
#
# QUESTION:
#   Given an m x n grid where 1 represents land and 0 water, return the
#   perimeter of the island (the grid is completely surrounded by water and
#   there is exactly one island).
#
#   Example:
#     Input : grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#     Output: 16
# =============================================================

islandPerimeter <- function(g) {
    R <- nrow(g); C <- ncol(g); p <- 0
    for (r in seq_len(R)) for (c in seq_len(C)) if (g[r,c] == 1) {
        p <- p + 4
        if (r > 1 && g[r-1, c] == 1) p <- p - 2
        if (c > 1 && g[r, c-1] == 1) p <- p - 2
    }
    p
}
print(islandPerimeter(matrix(c(0,1,0,0, 1,1,1,0, 0,1,0,0, 1,1,0,0), nrow=4, byrow=TRUE)))
