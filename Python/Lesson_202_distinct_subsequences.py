# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 202 -- Distinct Subsequences
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 101
# =============================================================
#
# QUESTION:
#   Number of distinct subsequences of s equal to t.
# =============================================================
def numDistinct(s,t):
    m,n=len(s),len(t); dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]+(dp[i-1][j-1] if s[i-1]==t[j-1] else 0)
    return dp[m][n]

if __name__=="__main__":
    print(numDistinct("rabbbit","rabbit"))
