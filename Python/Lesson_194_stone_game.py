# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 194 -- Stone Game
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 97
# =============================================================
#
# QUESTION:
#   Two players take stones from either end. Both play optimally. Return true if Alice wins.
# =============================================================
def stoneGame(p):
    n=len(p); dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=p[i]
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            dp[i][j]=max(p[i]-dp[i+1][j], p[j]-dp[i][j-1])
    return dp[0][n-1]>0

if __name__=="__main__":
    print(stoneGame([5,3,4,5]))
