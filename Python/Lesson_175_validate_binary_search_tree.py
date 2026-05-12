# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 175 -- Validate Binary Search Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 88
# =============================================================
#
# QUESTION:
#   Determine if a binary tree is a valid BST.
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def isValidBST(root):
    def rec(n,lo,hi):
        if not n: return True
        if not(lo<n.v<hi): return False
        return rec(n.l,lo,n.v) and rec(n.r,n.v,hi)
    return rec(root,float('-inf'),float('inf'))

if __name__=="__main__":
    r=N(2,N(1),N(3))
    print(isValidBST(r))
    r2=N(5,N(1),N(4,N(3),N(6)))
    print(isValidBST(r2))
