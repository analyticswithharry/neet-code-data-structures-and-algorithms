# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 180 -- House Robber III
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 90
# =============================================================
#
# QUESTION:
#   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
# =============================================================
rob <- function(root){ rec<-function(n){ if(is.null(n)) return(c(0,0)); l<-rec(n$l); r<-rec(n$r); c(n$v+l[2]+r[2], max(l)+max(r)) }; max(rec(root)) }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(rob(n(3,n(2,NULL,n(3)),n(3,NULL,n(1)))),"\n")
