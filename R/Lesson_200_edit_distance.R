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
minDistance <- function(a,b){ m<-nchar(a); n<-nchar(b); dp<-matrix(0,m+1,n+1); for(i in 0:m) dp[i+1,1]<-i; for(j in 0:n) dp[1,j+1]<-j; if(m>=1) for(i in 1:m) for(j in 1:n){ if(substr(a,i,i)==substr(b,j,j)) dp[i+1,j+1]<-dp[i,j] else dp[i+1,j+1]<-1+min(dp[i,j+1],dp[i+1,j],dp[i,j]) }; dp[m+1,n+1] }
cat(minDistance("horse","ros"),"\n")
