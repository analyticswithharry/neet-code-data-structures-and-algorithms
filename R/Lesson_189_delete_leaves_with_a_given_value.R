# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 189 -- Delete Leaves With a Given Value
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 95
# =============================================================
#
# QUESTION:
#   Delete all leaf nodes with a given target value (cascade).
# =============================================================
rem <- function(n,t){ if(is.null(n)) return(NULL); n$l<-rem(n$l,t); n$r<-rem(n$r,t); if(is.null(n$l)&&is.null(n$r)&&n$v==t) return(NULL); n }
nd <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
print(rem(nd(1,nd(2,nd(2)),nd(3,nd(2),nd(4))),2))
