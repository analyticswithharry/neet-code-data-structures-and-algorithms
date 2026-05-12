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
stoneGame <- function(p){ n<-length(p); dp<-matrix(0,n,n); for(i in 1:n) dp[i,i]<-p[i]; if(n>=2) for(L in 2:n) for(i in 1:(n-L+1)){ j<-i+L-1; dp[i,j]<-max(p[i]-dp[i+1,j], p[j]-dp[i,j-1]) }; dp[1,n]>0 }
cat(stoneGame(c(5,3,4,5)),"\n")
