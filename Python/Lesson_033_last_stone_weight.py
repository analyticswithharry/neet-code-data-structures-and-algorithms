# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 033 -- Last Stone Weight
# Category   : Heap Priority Queue
# Difficulty : Easy
# Study Plan : Day 17
# =============================================================
#
# QUESTION:
#   You are given an array of stones. On each turn pick the two heaviest
#   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
#   and y becomes y - x. Return the weight of the last remaining stone (or 0).
#
#   Example:
#     Input : [2,7,4,1,8,1]   Output: 1
# =============================================================

import heapq
class Solution:
    def lastStoneWeight(self, stones):
        h = [-s for s in stones]; heapq.heapify(h)
        while len(h) > 1:
            y = -heapq.heappop(h); x = -heapq.heappop(h)
            if y != x: heapq.heappush(h, -(y - x))
        return -h[0] if h else 0

if __name__ == "__main__":
    print(Solution().lastStoneWeight([2,7,4,1,8,1]))  # 1
