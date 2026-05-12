# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 188 -- Design Circular Queue
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 94
# =============================================================
#
# QUESTION:
#   Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.
# =============================================================
class CQ:
    def __init__(s,k): s.a=[0]*k; s.k=k; s.head=0; s.cnt=0
    def enQueue(s,v):
        if s.cnt==s.k: return False
        s.a[(s.head+s.cnt)%s.k]=v; s.cnt+=1; return True
    def deQueue(s):
        if s.cnt==0: return False
        s.head=(s.head+1)%s.k; s.cnt-=1; return True
    def Front(s): return -1 if s.cnt==0 else s.a[s.head]
    def Rear(s): return -1 if s.cnt==0 else s.a[(s.head+s.cnt-1)%s.k]
    def isEmpty(s): return s.cnt==0
    def isFull(s): return s.cnt==s.k

if __name__=="__main__":
    q=CQ(3); print(q.enQueue(1),q.enQueue(2),q.enQueue(3),q.enQueue(4))
    print(q.Rear(),q.isFull(),q.deQueue(),q.enQueue(4),q.Rear())
