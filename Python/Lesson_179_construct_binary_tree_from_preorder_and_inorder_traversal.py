# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 90
# =============================================================
#
# QUESTION:
#   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def build(pre,ino):
    idx={v:i for i,v in enumerate(ino)}
    it=iter(pre)
    def rec(lo,hi):
        if lo>hi: return None
        v=next(it); k=idx[v]
        n=N(v); n.l=rec(lo,k-1); n.r=rec(k+1,hi); return n
    return rec(0,len(ino)-1)

def pre_order(n):
    if not n: return []
    return [n.v]+pre_order(n.l)+pre_order(n.r)

if __name__=="__main__":
    r=build([3,9,20,15,7],[9,3,15,20,7])
    print(pre_order(r))
