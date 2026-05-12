# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 176 -- Kth Smallest Element In a Bst
# Category   : Trees
# Difficulty : Medium
# Study Plan : Day 88
# =============================================================
#
# QUESTION:
#   Return the kth smallest value in a BST (1-indexed).
# =============================================================
kth <- function(root,k){ st<-list(); cur<-root; while(!is.null(cur)||length(st)>0){ while(!is.null(cur)){ st[[length(st)+1]]<-cur; cur<-cur$l }; cur<-st[[length(st)]]; st[[length(st)]]<-NULL; k<-k-1; if(k==0) return(cur$v); cur<-cur$r } }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(kth(n(3,n(1,NULL,n(2)),n(4)),1),"\n")
