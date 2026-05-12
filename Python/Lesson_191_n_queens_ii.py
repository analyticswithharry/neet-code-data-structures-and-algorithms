# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 191 -- N Queens II
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 96
# =============================================================
#
# QUESTION:
#   Return number of distinct solutions for n-queens.
# =============================================================
def totalNQueens(n):
    cnt=[0]; cols=set(); d1=set(); d2=set()
    def bt(r):
        if r==n: cnt[0]+=1; return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c); bt(r+1)
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    bt(0); return cnt[0]

if __name__=="__main__":
    print(totalNQueens(4))
    print(totalNQueens(8))
