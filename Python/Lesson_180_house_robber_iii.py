# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 180 -- House Robber III
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 90
# =============================================================
#
# QUESTION:
#   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def rob(root):
    def rec(n):
        if not n: return (0,0)
        l=rec(n.l); r=rec(n.r)
        with_n=n.v+l[1]+r[1]
        wo_n=max(l)+max(r)
        return (with_n,wo_n)
    return max(rec(root))

if __name__=="__main__":
    r=N(3,N(2,None,N(3)),N(3,None,N(1)))
    print(rob(r))
