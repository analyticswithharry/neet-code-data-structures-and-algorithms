# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 091 -- Single Threaded CPU
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 46
# =============================================================
#
# QUESTION:
#   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
# =============================================================

import heapq
class Solution:
    def getOrder(self, tasks):
        idx = sorted(range(len(tasks)), key=lambda i: tasks[i][0])
        h=[]; res=[]; t=0; i=0
        while i < len(idx) or h:
            if not h:
                t = max(t, tasks[idx[i]][0])
            while i < len(idx) and tasks[idx[i]][0] <= t:
                heapq.heappush(h, (tasks[idx[i]][1], idx[i])); i += 1
            p, j = heapq.heappop(h); t += p; res.append(j)
        return res

if __name__ == "__main__":
    print(Solution().getOrder([[1,2],[2,4],[3,2],[4,1]]))
