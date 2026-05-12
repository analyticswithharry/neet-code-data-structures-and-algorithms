# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 102 -- Longest Common Subsequence
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 51
# =============================================================
#
# QUESTION:
#   Given two strings text1 and text2, return the length of their longest common subsequence.
# =============================================================

class Solution:
    def longestCommonSubsequence(self, a, b):
        m,n=len(a),len(b)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if a[i]==b[j]: dp[i+1][j+1]=dp[i][j]+1
                else: dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]

if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("abcde","ace"))
