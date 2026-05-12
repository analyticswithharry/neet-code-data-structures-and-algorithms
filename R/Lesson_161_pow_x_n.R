# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 161 -- Pow x n
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 81
# =============================================================
#
# QUESTION:
#   Implement pow(x, n) — x raised to the n-th power.
# =============================================================
myPow <- function(x,n){ if(n<0){ x<-1/x; n<--n }; r<-1.0; while(n>0){ if(bitwAnd(n,1)==1) r<-r*x; x<-x*x; n<-bitwShiftR(n,1) }; r }
cat(myPow(2,10),"\n"); cat(myPow(2,-2),"\n")
