# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 187 -- Reverse Linked List II
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 94
# =============================================================
#
# QUESTION:
#   Reverse the nodes of the list from position left to right (1-indexed).
# =============================================================
reverseBetween <- function(a,L,R){ x<-a[L:R]; a[L:R]<-rev(x); a }
cat(reverseBetween(c(1,2,3,4,5),2,4),"\n")
