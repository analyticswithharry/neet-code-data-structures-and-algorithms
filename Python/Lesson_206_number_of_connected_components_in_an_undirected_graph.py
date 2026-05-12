# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 206 -- Number of Connected Components In An Undirected Graph
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 103
# =============================================================
#
# QUESTION:
#   Given n nodes and undirected edges, return the number of connected components.
# =============================================================
def countComponents(n,edges):
    par=list(range(n)); cnt=n
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra!=rb: par[ra]=rb; cnt-=1
    return cnt

if __name__=="__main__":
    print(countComponents(5,[[0,1],[1,2],[3,4]]))
    print(countComponents(5,[[0,1],[1,2],[2,3],[3,4]]))
