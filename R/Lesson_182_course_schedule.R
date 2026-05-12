# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 182 -- Course Schedule
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 91
# =============================================================
#
# QUESTION:
#   Given prerequisites pairs, can all courses be finished (no cycle)?
# =============================================================
canFinish <- function(n,pre){ g<-vector("list",n); ind<-rep(0,n); for(p in pre){ g[[p[2]+1]]<-c(g[[p[2]+1]],p[1]+1); ind[p[1]+1]<-ind[p[1]+1]+1 }; q<-which(ind==0); cnt<-0; while(length(q)>0){ x<-q[1]; q<-q[-1]; cnt<-cnt+1; for(y in g[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; cnt==n }
cat(canFinish(2,list(c(1,0))),"\n"); cat(canFinish(2,list(c(1,0),c(0,1))),"\n")
