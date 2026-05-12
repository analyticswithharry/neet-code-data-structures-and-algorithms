# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 203 -- Course Schedule II
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 102
# =============================================================
#
# QUESTION:
#   Return any topological ordering of courses, or empty array if impossible.
# =============================================================
findOrder <- function(n,pre){ g<-vector("list",n); ind<-rep(0,n); for(p in pre){ g[[p[2]+1]]<-c(g[[p[2]+1]],p[1]+1); ind[p[1]+1]<-ind[p[1]+1]+1 }; q<-which(ind==0); res<-c(); while(length(q)>0){ x<-q[1]; q<-q[-1]; res<-c(res,x-1); for(y in g[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; if(length(res)==n) res else c() }
cat(findOrder(4,list(c(1,0),c(2,0),c(3,1),c(3,2))),"\n")
