# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 176 -- Kth Smallest Element In a Bst
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 88
# =============================================================
#
# QUESTION:
#   Return the kth smallest value in a BST (1-indexed).
# =============================================================
class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def kth(root,k):
    st=[]; cur=root
    while cur or st:
        while cur: st.append(cur); cur=cur.l
        cur=st.pop(); k-=1
        if k==0: return cur.v
        cur=cur.r

if __name__=="__main__":
    r=N(3,N(1,None,N(2)),N(4))
    print(kth(r,1))
    print(kth(r,3))
