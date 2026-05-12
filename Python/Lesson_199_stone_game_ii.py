# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 199 -- Stone Game II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 100
# =============================================================
#
# QUESTION:
#   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
# =============================================================
def stoneGameII(p):
    n=len(p); suf=[0]*(n+1)
    for i in range(n-1,-1,-1): suf[i]=suf[i+1]+p[i]
    memo={}
    def dfs(i,M):
        if i+2*M>=n: return suf[i]
        if (i,M) in memo: return memo[(i,M)]
        best=0
        for x in range(1,2*M+1):
            best=max(best, suf[i]-dfs(i+x, max(M,x)))
        memo[(i,M)]=best; return best
    return dfs(0,1)

if __name__=="__main__":
    print(stoneGameII([2,7,9,4,4]))
