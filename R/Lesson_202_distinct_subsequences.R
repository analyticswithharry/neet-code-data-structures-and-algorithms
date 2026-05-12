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
numDistinct <- function(s,t){ m<-nchar(s); n<-nchar(t); dp<-matrix(0,m+1,n+1); for(i in 0:m) dp[i+1,1]<-1; if(m>=1) for(i in 1:m) for(j in 1:n){ dp[i+1,j+1]<-dp[i,j+1]; if(substr(s,i,i)==substr(t,j,j)) dp[i+1,j+1]<-dp[i+1,j+1]+dp[i,j] }; dp[m+1,n+1] }
cat(numDistinct("rabbbit","rabbit"),"\n")
