# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 198 -- Find in Mountain Array
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 99
# =============================================================
#
# QUESTION:
#   Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.
# =============================================================
findInMountainArray <- function(t,a){ idx<-which(a==t); if(length(idx)==0) -1 else idx[1]-1 }
cat(findInMountainArray(3,c(1,2,3,4,5,3,1)),"\n")
