# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 204 -- Graph Valid Tree
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 102
# =============================================================
#
# QUESTION:
#   Given n nodes and edges, determine if they form a tree (connected and no cycles).
# =============================================================
validTree <- function(n,edges){ if(length(edges)!=n-1) return(FALSE); par<-0:(n-1); find<-function(x){ while(par[x+1]!=x){ par[x+1]<<-par[par[x+1]+1]; x<-par[x+1] }; x }; for(e in edges){ ra<-find(e[1]); rb<-find(e[2]); if(ra==rb) return(FALSE); par[ra+1]<<-rb }; TRUE }
cat(validTree(5,list(c(0,1),c(0,2),c(0,3),c(1,4))),"\n")
