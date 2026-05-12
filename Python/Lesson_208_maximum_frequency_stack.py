# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 208 -- Maximum Frequency Stack
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 104
# =============================================================
#
# QUESTION:
#   Push/pop a stack returning the most-frequent element (ties: most recent).
# =============================================================
from collections import defaultdict
class FreqStack:
    def __init__(s): s.f=defaultdict(int); s.g=defaultdict(list); s.maxf=0
    def push(s,v): s.f[v]+=1; s.maxf=max(s.maxf,s.f[v]); s.g[s.f[v]].append(v)
    def pop(s):
        v=s.g[s.maxf].pop(); s.f[v]-=1
        if not s.g[s.maxf]: s.maxf-=1
        return v

if __name__=="__main__":
    fs=FreqStack()
    for x in [5,7,5,7,4,5]: fs.push(x)
    print([fs.pop() for _ in range(4)])
