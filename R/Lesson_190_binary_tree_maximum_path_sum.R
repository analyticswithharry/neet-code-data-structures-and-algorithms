# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 190 -- Binary Tree Maximum Path Sum
# Category   : Trees
# Difficulty : Hard
# Study Plan : Day 95
# =============================================================
#
# QUESTION:
#   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
# =============================================================
res <- -Inf
dfs <- function(n){ if(is.null(n)) return(0); l<-max(0,dfs(n$l)); r<-max(0,dfs(n$r)); res<<-max(res,n$v+l+r); n$v+max(l,r) }
maxPathSum <- function(r){ res<<- -Inf; dfs(r); res }
nd <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(maxPathSum(nd(-10,nd(9),nd(20,nd(15),nd(7)))),"\n")
