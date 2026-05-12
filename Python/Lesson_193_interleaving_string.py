# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 193 -- Interleaving String
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 97
# =============================================================
#
# QUESTION:
#   Determine whether s3 can be formed by interleaving s1 and s2.
# =============================================================
def isInterleave(a,b,c):
    if len(a)+len(b)!=len(c): return False
    dp=[[False]*(len(b)+1) for _ in range(len(a)+1)]
    dp[0][0]=True
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i and a[i-1]==c[i+j-1]: dp[i][j]|=dp[i-1][j]
            if j and b[j-1]==c[i+j-1]: dp[i][j]|=dp[i][j-1]
    return dp[len(a)][len(b)]

if __name__=="__main__":
    print(isInterleave("aabcc","dbbca","aadbbcbcac"))
    print(isInterleave("aabcc","dbbca","aadbbbaccc"))
