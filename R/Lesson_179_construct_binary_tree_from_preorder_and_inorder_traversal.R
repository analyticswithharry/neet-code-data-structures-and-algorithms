# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 90
# =============================================================
#
# QUESTION:
#   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
# =============================================================
build <- function(pre,ino){ idx<-setNames(seq_along(ino)-1,ino); p<-1; rec<-function(lo,hi){ if(lo>hi) return(NULL); v<-pre[p]; p<<-p+1; k<-idx[[as.character(v)]]; list(v=v,l=rec(lo,k-1),r=rec(k+1,hi)) }; rec(0,length(ino)-1) }
pre_order <- function(n){ if(is.null(n)) return(c()); c(n$v,pre_order(n$l),pre_order(n$r)) }
cat(pre_order(build(c(3,9,20,15,7),c(9,3,15,20,7))),"\n")
