# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 210 -- Dota2 Senate
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 105
# =============================================================
#
# QUESTION:
#   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
# =============================================================
from collections import deque
def predictPartyVictory(s):
    R=deque(); D=deque(); n=len(s)
    for i,ch in enumerate(s): (R if ch=='R' else D).append(i)
    while R and D:
        r=R.popleft(); d=D.popleft()
        if r<d: R.append(r+n)
        else: D.append(d+n)
    return "Radiant" if R else "Dire"

if __name__=="__main__":
    print(predictPartyVictory("RD"))
    print(predictPartyVictory("RDD"))
