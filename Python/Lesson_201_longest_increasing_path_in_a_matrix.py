# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 201 -- Longest Increasing Path In a Matrix
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 101
# =============================================================
#
# QUESTION:
#   Find length of the longest strictly-increasing path in a 2D grid.
# =============================================================
def longestIncreasingPath(g):
    if not g: return 0
    R,C=len(g),len(g[0]); memo=[[0]*C for _ in range(R)]
    def dfs(r,c):
        if memo[r][c]: return memo[r][c]
        best=1
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and g[nr][nc]>g[r][c]:
                best=max(best,1+dfs(nr,nc))
        memo[r][c]=best; return best
    return max(dfs(r,c) for r in range(R) for c in range(C))

if __name__=="__main__":
    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
