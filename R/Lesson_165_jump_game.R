# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 165 -- Jump Game
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 83
# =============================================================
#
# QUESTION:
#   Each element is max jump length from that position. Return true iff you can reach the last index from index 0.
# =============================================================
canJump <- function(a){ r<-0; for(i in seq_along(a)){ if((i-1)>r) return(FALSE); r<-max(r,(i-1)+a[i]) }; TRUE }
cat(canJump(c(2,3,1,1,4)),"\n"); cat(canJump(c(3,2,1,0,4)),"\n")
