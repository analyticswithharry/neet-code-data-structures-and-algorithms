# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 167 -- Coin Change
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 84
# =============================================================
#
# QUESTION:
#   Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.
# =============================================================
coinChange <- function(coins,amt){ INF<-1e9; dp<-rep(INF,amt+1); dp[1]<-0; if(amt>=1) for(a in 1:amt){ for(c in coins) if(c<=a) dp[a+1]<-min(dp[a+1],dp[a-c+1]+1) }; if(dp[amt+1]>=INF) -1 else dp[amt+1] }
cat(coinChange(c(1,2,5),11),"\n"); cat(coinChange(c(2),3),"\n")
