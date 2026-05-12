# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 174 -- Surrounded Regions
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 87
# =============================================================
#
# QUESTION:
#   Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).
# =============================================================
def solve(b):
    if not b: return
    R,C=len(b),len(b[0])
    def dfs(r,c):
        if r<0 or r>=R or c<0 or c>=C or b[r][c]!='O': return
        b[r][c]='S'
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
    for r in range(R):
        dfs(r,0); dfs(r,C-1)
    for c in range(C):
        dfs(0,c); dfs(R-1,c)
    for r in range(R):
        for c in range(C):
            b[r][c]='O' if b[r][c]=='S' else 'X'

if __name__=="__main__":
    g=[['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
    solve(g); print(g)
