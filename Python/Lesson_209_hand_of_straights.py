# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 209 -- Hand of Straights
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 105
# =============================================================
#
# QUESTION:
#   Can hand be rearranged into groups of size W of consecutive cards?
# =============================================================
from collections import Counter
def isNStraightHand(h,W):
    if len(h)%W: return False
    c=Counter(h)
    for x in sorted(c):
        if c[x]>0:
            cnt=c[x]
            for k in range(W):
                if c[x+k]<cnt: return False
                c[x+k]-=cnt
    return True

if __name__=="__main__":
    print(isNStraightHand([1,2,3,6,2,3,4,7,8],3))
    print(isNStraightHand([1,2,3,4,5],4))
