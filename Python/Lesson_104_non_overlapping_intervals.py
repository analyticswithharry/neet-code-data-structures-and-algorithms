# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 104 -- Non Overlapping Intervals
# Category   : Intervals
# Difficulty : Medium
# Study Plan : Day 52
# =============================================================
#
# QUESTION:
#   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
# =============================================================

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1]); end=float('-inf'); rm=0
        for s,e in intervals:
            if s>=end: end=e
            else: rm+=1
        return rm

if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
