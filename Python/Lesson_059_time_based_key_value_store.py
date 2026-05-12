# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 059 -- Time Based Key Value Store
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 29
# =============================================================
#
# QUESTION:
#   Design a time-based key-value data structure that supports
#   set(key, value, timestamp) and get(key, timestamp), where get returns
#   the value with the largest timestamp <= the given timestamp.
# =============================================================

from bisect import bisect_right
class TimeMap:
    def __init__(self): self.d = {}
    def set(self, k, v, t):
        self.d.setdefault(k, []).append((t, v))
    def get(self, k, t):
        if k not in self.d: return ""
        arr = self.d[k]
        i = bisect_right(arr, (t, chr(127)))
        return arr[i-1][1] if i else ""

if __name__ == "__main__":
    tm = TimeMap(); tm.set("foo","bar",1)
    print(tm.get("foo",1)); print(tm.get("foo",3))
    tm.set("foo","bar2",4); print(tm.get("foo",4)); print(tm.get("foo",5))
