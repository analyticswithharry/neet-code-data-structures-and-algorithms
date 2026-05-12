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

import heapq
class Solution:
    def kClosest(self, points, k):
        h = []
        for x, y in points:
            heapq.heappush(h, (-(x*x + y*y), [x,y]))
            if len(h) > k: heapq.heappop(h)
        return [p for _, p in h]

if __name__ == "__main__":
    print(Solution().kClosest([[1,3],[-2,2]], 1))
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
