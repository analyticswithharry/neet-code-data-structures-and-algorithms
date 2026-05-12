# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 196 -- Trapping Rain Water
# Category   : Two Pointers
# Difficulty : Hard
# Study Plan : Day 98
# =============================================================
#
# QUESTION:
#   Compute total water trapped between bars given heights.
# =============================================================
trap <- function(h){ l<-1; r<-length(h); lm<-0; rm<-0; res<-0; while(l<r){ if(h[l]<h[r]){ if(h[l]>=lm) lm<-h[l] else res<-res+lm-h[l]; l<-l+1 } else { if(h[r]>=rm) rm<-h[r] else res<-res+rm-h[r]; r<-r-1 } }; res }
cat(trap(c(0,1,0,2,1,0,1,3,2,1,2,1)),"\n")
