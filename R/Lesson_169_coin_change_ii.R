# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 169 -- Coin Change II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 85
# =============================================================
#
# QUESTION:
#   Number of distinct combinations of coins (unlimited) summing to amount.
# =============================================================
change <- function(amt,coins){ dp<-rep(0,amt+1); dp[1]<-1; for(c in coins) if(c<=amt) for(a in c:amt) dp[a+1]<-dp[a+1]+dp[a-c+1]; dp[amt+1] }
cat(change(5,c(1,2,5)),"\n"); cat(change(3,c(2)),"\n")
