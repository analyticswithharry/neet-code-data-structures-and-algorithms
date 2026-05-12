# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 025 -- Path with Minimum Effort
# Category   : Advanced Graphs
# Difficulty : Medium
# Study Plan : Day 13
# =============================================================
#
# QUESTION:
#   Given an m x n grid of heights, find a path from top-left to
#   bottom-right that minimizes the maximum absolute difference in heights
#   between consecutive cells along the path.
#
#   Example:
#     Input : heights = [[1,2,2],[3,8,2],[5,3,5]]
#     Output: 2
# =============================================================

minimumEffortPath <- function(h) {
    R <- nrow(h); C <- ncol(h)
    dist <- matrix(Inf, R, C); dist[1,1] <- 0
    # Simple Dijkstra with repeated min scan (small inputs only)
    visited <- matrix(FALSE, R, C)
    for (step in 1:(R*C)) {
        bestD <- Inf; br <- 0; bc <- 0
        for (i in 1:R) for (j in 1:C) if (!visited[i,j] && dist[i,j] < bestD) { bestD <- dist[i,j]; br <- i; bc <- j }
        if (br == 0) break
        if (br == R && bc == C) return(bestD)
        visited[br, bc] <- TRUE
        for (d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))) {
            nr <- br + d[1]; nc <- bc + d[2]
            if (nr>=1 && nr<=R && nc>=1 && nc<=C) {
                nd <- max(bestD, abs(h[nr,nc] - h[br,bc]))
                if (nd < dist[nr,nc]) dist[nr,nc] <- nd
            }
        }
    }
    dist[R, C]
}
print(minimumEffortPath(matrix(c(1,2,2,3,8,2,5,3,5), nrow=3, byrow=TRUE)))
