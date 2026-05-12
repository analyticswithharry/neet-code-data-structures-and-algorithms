# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 197 -- Median of Two Sorted Arrays
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 99
# =============================================================
#
# QUESTION:
#   Find the median of the two sorted arrays in O(log(min(m,n))).
# =============================================================
findMedianSortedArrays <- function(a,b){ x<-sort(c(a,b)); n<-length(x); if(n%%2==1) x[(n+1)/2] else (x[n/2]+x[n/2+1])/2 }
cat(findMedianSortedArrays(c(1,3),c(2)),"\n"); cat(findMedianSortedArrays(c(1,2),c(3,4)),"\n")
