# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 020 -- K Closest Points to Origin
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 10
# =============================================================
#
# QUESTION:
#   Given an array of points where points[i] = [xi, yi] and an integer k,
#   return the k closest points to the origin (0, 0). Distance is Euclidean.
#
#   Example:
#     Input : points = [[1,3],[-2,2]], k = 1
#     Output: [[-2,2]]
# =============================================================

kClosest <- function(points, k) {
    d <- sapply(points, function(p) p[1]^2 + p[2]^2)
    points[order(d)][1:k]
}
print(kClosest(list(c(1,3), c(-2,2)), 1))
print(kClosest(list(c(3,3), c(5,-1), c(-2,4)), 2))
