# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 107 -- Implement Queue using Stacks
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 54
# =============================================================
#
# QUESTION:
#   Implement a FIFO queue using only two stacks.
# =============================================================

class MyQueue:
    def __init__(self): self.a=[]; self.b=[]
    def push(self, x): self.a.append(x)
    def pop(self):
        if not self.b:
            while self.a: self.b.append(self.a.pop())
        return self.b.pop()
    def peek(self):
        if not self.b:
            while self.a: self.b.append(self.a.pop())
        return self.b[-1]
    def empty(self): return not self.a and not self.b

if __name__ == "__main__":
    q=MyQueue(); q.push(1); q.push(2); print(q.peek()); print(q.pop()); print(q.empty())
