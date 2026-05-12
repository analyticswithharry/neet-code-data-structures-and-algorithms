# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 175 -- Validate Binary Search Tree
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 88
# =============================================================
#
# QUESTION:
#   Determine if a binary tree is a valid BST.
# =============================================================
isValidBST <- function(n,lo=-Inf,hi=Inf){ if(is.null(n)) return(TRUE); if(!(n$v>lo && n$v<hi)) return(FALSE); isValidBST(n$l,lo,n$v) && isValidBST(n$r,n$v,hi) }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(isValidBST(n(2,n(1),n(3))),"\n")
