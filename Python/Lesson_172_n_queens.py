# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 172 -- N Queens
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 86
# =============================================================
#
# QUESTION:
#   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
# =============================================================
def totalNQueens(n):
    cnt=[0]; cols=set(); d1=set(); d2=set()
    def bt(r):
        if r==n: cnt[0]+=1; return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c)
            bt(r+1)
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    bt(0); return cnt[0]

if __name__=="__main__":
    print(totalNQueens(4))
    print(totalNQueens(6))
