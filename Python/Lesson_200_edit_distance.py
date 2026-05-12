# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 200 -- Edit Distance
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 100
# =============================================================
#
# QUESTION:
#   Min number of insert/delete/replace ops to convert s1 to s2.
# =============================================================
def minDistance(a,b):
    m,n=len(a),len(b); dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]
            else: dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]

if __name__=="__main__":
    print(minDistance("horse","ros"))
    print(minDistance("intention","execution"))
