# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 182 -- Course Schedule
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 91
# =============================================================
#
# QUESTION:
#   Given prerequisites pairs, can all courses be finished (no cycle)?
# =============================================================
def canFinish(n,pre):
    from collections import defaultdict,deque
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[b].append(a); ind[a]+=1
    q=deque(i for i in range(n) if ind[i]==0); cnt=0
    while q:
        x=q.popleft(); cnt+=1
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return cnt==n

if __name__=="__main__":
    print(canFinish(2,[[1,0]]))
    print(canFinish(2,[[1,0],[0,1]]))
