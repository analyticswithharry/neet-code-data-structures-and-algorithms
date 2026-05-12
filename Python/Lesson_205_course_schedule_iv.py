# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 205 -- Course Schedule IV
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 103
# =============================================================
#
# QUESTION:
#   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
# =============================================================
def checkIfPrerequisite(n,pre,queries):
    reach=[[False]*n for _ in range(n)]
    from collections import defaultdict
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[a].append(b); ind[b]+=1; reach[a][b]=True
    from collections import deque
    q=deque(i for i in range(n) if ind[i]==0); order=[]
    while q:
        x=q.popleft(); order.append(x)
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    for x in order:
        for y in g[x]:
            for k in range(n):
                if reach[k][x]: reach[k][y]=True
    return [reach[u][v] for u,v in queries]

if __name__=="__main__":
    print(checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))
