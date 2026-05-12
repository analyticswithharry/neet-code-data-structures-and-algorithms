# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 206 -- Number of Connected Components In An Undirected Graph
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 103
# =============================================================
#
# QUESTION:
#   Given n nodes and undirected edges, return the number of connected components.
# =============================================================
countComponents <- function(n,edges){ par<-0:(n-1); cnt<-n; find<-function(x){ while(par[x+1]!=x){ par[x+1]<<-par[par[x+1]+1]; x<-par[x+1] }; x }; for(e in edges){ ra<-find(e[1]); rb<-find(e[2]); if(ra!=rb){ par[ra+1]<<-rb; cnt<<-cnt-1 } }; cnt }
cat(countComponents(5,list(c(0,1),c(1,2),c(3,4))),"\n")
