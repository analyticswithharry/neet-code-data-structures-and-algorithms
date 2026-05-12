# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 204 -- Graph Valid Tree
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 102
# =============================================================
#
# QUESTION:
#   Given n nodes and edges, determine if they form a tree (connected and no cycles).
# =============================================================
def validTree(n,edges):
    if len(edges)!=n-1: return False
    par=list(range(n))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra==rb: return False
        par[ra]=rb
    return True

if __name__=="__main__":
    print(validTree(5,[[0,1],[0,2],[0,3],[1,4]]))
    print(validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]))
