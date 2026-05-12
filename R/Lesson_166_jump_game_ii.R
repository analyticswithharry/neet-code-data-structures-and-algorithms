# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 166 -- Jump Game II
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 83
# =============================================================
#
# QUESTION:
#   Return the minimum number of jumps to reach the last index. Assume reachable.
# =============================================================
jump <- function(a){ j<-0; cur<-0; far<-0; n<-length(a); for(i in 1:(n-1)){ far<-max(far,(i-1)+a[i]); if((i-1)==cur){ j<-j+1; cur<-far } }; j }
cat(jump(c(2,3,1,1,4)),"\n"); cat(jump(c(2,3,0,1,4)),"\n")
