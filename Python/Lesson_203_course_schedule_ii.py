# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 203 -- Course Schedule II
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 102
# =============================================================
#
# QUESTION:
#   Return any topological ordering of courses, or empty array if impossible.
# =============================================================
def findOrder(n,pre):
    from collections import defaultdict,deque
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[b].append(a); ind[a]+=1
    q=deque(i for i in range(n) if ind[i]==0); res=[]
    while q:
        x=q.popleft(); res.append(x)
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return res if len(res)==n else []

if __name__=="__main__":
    print(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
