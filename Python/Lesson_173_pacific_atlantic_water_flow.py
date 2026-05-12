# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 173 -- Pacific Atlantic Water Flow
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 87
# =============================================================
#
# QUESTION:
#   Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).
# =============================================================
def pacificAtlantic(h):
    if not h: return []
    R,C=len(h),len(h[0])
    pac=[[False]*C for _ in range(R)]; atl=[[False]*C for _ in range(R)]
    def dfs(r,c,seen):
        seen[r][c]=True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and not seen[nr][nc] and h[nr][nc]>=h[r][c]:
                dfs(nr,nc,seen)
    for c in range(C):
        dfs(0,c,pac); dfs(R-1,c,atl)
    for r in range(R):
        dfs(r,0,pac); dfs(r,C-1,atl)
    return [[r,c] for r in range(R) for c in range(C) if pac[r][c] and atl[r][c]]

if __name__=="__main__":
    print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
