# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 103 -- Merge Intervals
# Category   : Intervals
# Difficulty : Medium
# Study Plan : Day 52
# =============================================================
#
# QUESTION:
#   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
# =============================================================

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0]); res=[]
        for s,e in intervals:
            if res and s <= res[-1][1]: res[-1][1]=max(res[-1][1], e)
            else: res.append([s,e])
        return res

if __name__ == "__main__":
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
