# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 190 -- Binary Tree Maximum Path Sum
# Category   : Trees
# Difficulty : Hard
# Study Plan : Day 95
# =============================================================
#
# QUESTION:
#   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def maxPathSum(root):
    res=[float('-inf')]
    def dfs(n):
        if not n: return 0
        l=max(0,dfs(n.l)); r=max(0,dfs(n.r))
        res[0]=max(res[0],n.v+l+r)
        return n.v+max(l,r)
    dfs(root); return res[0]

if __name__=="__main__":
    print(maxPathSum(N(1,N(2),N(3))))
    print(maxPathSum(N(-10,N(9),N(20,N(15),N(7)))))
