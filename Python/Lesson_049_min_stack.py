# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 049 -- Min Stack
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 24
# =============================================================
#
# QUESTION:
#   Design a stack supporting push, pop, top, and getMin in O(1).
# =============================================================

class MinStack:
    def __init__(self):
        self.s = []; self.m = []
    def push(self, val):
        self.s.append(val)
        self.m.append(val if not self.m else min(val, self.m[-1]))
    def pop(self): self.s.pop(); self.m.pop()
    def top(self): return self.s[-1]
    def getMin(self): return self.m[-1]

if __name__ == "__main__":
    s = MinStack(); s.push(-2); s.push(0); s.push(-3)
    print(s.getMin()); s.pop(); print(s.top()); print(s.getMin())
