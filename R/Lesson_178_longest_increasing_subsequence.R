# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 178 -- Longest Increasing Subsequence
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 89
# =============================================================
#
# QUESTION:
#   Length of the longest strictly-increasing subsequence.
# =============================================================
LIS <- function(a){ t<-c(); for(x in a){ i<-findInterval(x-1,t)+1; if(i>length(t)) t<-c(t,x) else t[i]<-x }; length(t) }
cat(LIS(c(10,9,2,5,3,7,101,18)),"\n")
