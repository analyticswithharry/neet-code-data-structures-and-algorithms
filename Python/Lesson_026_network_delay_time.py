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

import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        for u,v,w in times: g[u].append((v,w))
        dist = {}
        h = [(0, k)]
        while h:
            d, u = heapq.heappop(h)
            if u in dist: continue
            dist[u] = d
            for v, w in g[u]:
                if v not in dist: heapq.heappush(h, (d+w, v))
        if len(dist) < n: return -1
        return max(dist.values())

if __name__ == "__main__":
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
