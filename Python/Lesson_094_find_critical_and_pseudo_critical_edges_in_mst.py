# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 47
# =============================================================
#
# QUESTION:
#   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
# =============================================================

class DSU:
    def __init__(self,n): self.p=list(range(n)); self.r=[0]*n; self.cnt=n
    def f(self,x):
        while self.p[x]!=x: self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def u(self,a,b):
        a,b=self.f(a),self.f(b)
        if a==b: return False
        if self.r[a]<self.r[b]: a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]: self.r[a]+=1
        self.cnt-=1; return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i,e in enumerate(edges): e.append(i)
        edges.sort(key=lambda e: e[2])
        def kruskal(skip=-1, force=-1):
            d=DSU(n); w=0
            if force>=0:
                u,v,wt,_ = edges[force]
                if not d.u(u,v): return float('inf')
                w += wt
            for i,(u,v,wt,_) in enumerate(edges):
                if i==skip: continue
                if d.u(u,v): w += wt
            return w if d.cnt==1 else float('inf')
        base = kruskal()
        crit, pseu = [], []
        for i,(u,v,wt,oi) in enumerate(edges):
            if kruskal(skip=i) > base: crit.append(oi)
            elif kruskal(force=i) == base: pseu.append(oi)
        return [crit, pseu]

if __name__ == "__main__":
    print(Solution().findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
