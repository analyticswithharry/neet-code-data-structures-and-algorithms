# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 187 -- Reverse Linked List II
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 94
# =============================================================
#
# QUESTION:
#   Reverse the nodes of the list from position left to right (1-indexed).
# =============================================================
class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def reverseBetween(h,L,R):
    d=N(0,h); pre=d
    for _ in range(L-1): pre=pre.n
    cur=pre.n
    for _ in range(R-L):
        nxt=cur.n; cur.n=nxt.n; nxt.n=pre.n; pre.n=nxt
    return d.n
def to_list(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
def from_list(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n

if __name__=="__main__":
    print(to_list(reverseBetween(from_list([1,2,3,4,5]),2,4)))
