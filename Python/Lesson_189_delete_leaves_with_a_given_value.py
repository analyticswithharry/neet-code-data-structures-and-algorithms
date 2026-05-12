# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 189 -- Delete Leaves With a Given Value
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 95
# =============================================================
#
# QUESTION:
#   Delete all leaf nodes with a given target value (cascade).
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def removeLeafNodes(root,t):
    if not root: return None
    root.l=removeLeafNodes(root.l,t)
    root.r=removeLeafNodes(root.r,t)
    if not root.l and not root.r and root.v==t: return None
    return root
def to_list(n):
    if not n: return None
    return [n.v,to_list(n.l),to_list(n.r)]

if __name__=="__main__":
    r=N(1,N(2,N(2)),N(3,N(2),N(4)))
    print(to_list(removeLeafNodes(r,2)))
