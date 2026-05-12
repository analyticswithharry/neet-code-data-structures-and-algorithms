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

longestCommonSubsequence <- function(a, b){
  m <- nchar(a); n <- nchar(b); dp <- matrix(0, m+1, n+1)
  ca <- strsplit(a,"")[[1]]; cb <- strsplit(b,"")[[1]]
  for (i in 1:m) for (j in 1:n){
    if (ca[i]==cb[j]) dp[i+1, j+1] <- dp[i,j] + 1
    else dp[i+1, j+1] <- max(dp[i, j+1], dp[i+1, j])
  }
  dp[m+1, n+1]
}
print(longestCommonSubsequence("abcde","ace"))
