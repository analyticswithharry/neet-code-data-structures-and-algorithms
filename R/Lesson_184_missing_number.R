# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 184 -- Missing Number
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 92
# =============================================================
#
# QUESTION:
#   Array contains n distinct numbers from [0,n]. Return the missing one.
# =============================================================
missing_num <- function(a){ x<-length(a); for(i in seq_along(a)) x<-bitwXor(x,bitwXor(i-1,a[i])); x }
cat(missing_num(c(3,0,1)),"\n"); cat(missing_num(c(9,6,4,2,3,5,7,0,1)),"\n")
