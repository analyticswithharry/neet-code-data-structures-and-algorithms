# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 181 -- Open The Lock
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 91
# =============================================================
#
# QUESTION:
#   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
# =============================================================
from collections import deque
def openLock(deadends,target):
    dead=set(deadends)
    if "0000" in dead: return -1
    if target=="0000": return 0
    seen={"0000"}; q=deque([("0000",0)])
    while q:
        s,d=q.popleft()
        for i in range(4):
            for delta in (-1,1):
                ns=s[:i]+str((int(s[i])+delta)%10)+s[i+1:]
                if ns==target: return d+1
                if ns not in seen and ns not in dead:
                    seen.add(ns); q.append((ns,d+1))
    return -1

if __name__=="__main__":
    print(openLock(["0201","0101","0102","1212","2002"],"0202"))
