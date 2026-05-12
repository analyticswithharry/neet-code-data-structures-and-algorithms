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

import heapq
class Solution:
    def minimumEffortPath(self, heights):
        R, C = len(heights), len(heights[0])
        dist = [[float('inf')] * C for _ in range(R)]
        dist[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            d, r, c = heapq.heappop(h)
            if r == R-1 and c == C-1: return d
            if d > dist[r][c]: continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C:
                    nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(h, (nd, nr, nc))
        return 0

if __name__ == "__main__":
    print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))  # 2
