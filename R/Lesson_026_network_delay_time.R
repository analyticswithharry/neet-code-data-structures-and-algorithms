# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 026 -- Network Delay Time
# Category   : Advanced Graphs
# Difficulty : Medium
# Study Plan : Day 13
# =============================================================
#
# QUESTION:
#   You are given a network of n nodes labeled from 1 to n. times[i] =
#   [u,v,w] means a signal takes w time from u to v. Starting from node k,
#   return the time it takes for all nodes to receive the signal. If
#   impossible, return -1.
#
#   Example:
#     Input : times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#     Output: 2
# =============================================================

networkDelayTime <- function(times, n, k) {
    INF <- .Machine$integer.max
    dist <- rep(INF, n); dist[k] <- 0
    visited <- rep(FALSE, n)
    g <- vector("list", n)
    for (t in times) g[[t[1]]] <- c(g[[t[1]]], list(c(t[2], t[3])))
    for (s in 1:n) {
        u <- which.min(ifelse(visited, INF, dist))
        if (dist[u] == INF) return(-1)
        visited[u] <- TRUE
        for (e in g[[u]]) {
            v <- e[1]; w <- e[2]
            if (!visited[v] && dist[u] + w < dist[v]) dist[v] <- dist[u] + w
        }
    }
    if (any(dist == INF)) return(-1)
    max(dist)
}
print(networkDelayTime(list(c(2,1,1), c(2,3,1), c(3,4,1)), 4, 2))
