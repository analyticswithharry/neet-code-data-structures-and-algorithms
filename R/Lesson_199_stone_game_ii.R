# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 199 -- Stone Game II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 100
# =============================================================
#
# QUESTION:
#   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
# =============================================================
stoneGameII <- function(p){ n<-length(p); suf<-rep(0,n+1); for(i in n:1) suf[i]<-suf[i+1]+p[i]; memo<-list(); dfs<-function(i,M){ if(i+2*M-1>=n) return(suf[i]); k<-paste(i,M); if(!is.null(memo[[k]])) return(memo[[k]]); best<-0; for(x in 1:(2*M)) best<-max(best,suf[i]-dfs(i+x,max(M,x))); memo[[k]]<<-best; best }; dfs(1,1) }
cat(stoneGameII(c(2,7,9,4,4)),"\n")
