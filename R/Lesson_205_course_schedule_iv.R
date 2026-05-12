# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 205 -- Course Schedule IV
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 103
# =============================================================
#
# QUESTION:
#   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
# =============================================================
checkIfPrerequisite <- function(n,pre,qs){ r<-matrix(FALSE,n,n); for(p in pre) r[p[1]+1,p[2]+1]<-TRUE; for(k in 1:n) for(i in 1:n) for(j in 1:n) if(r[i,k]&&r[k,j]) r[i,j]<-TRUE; sapply(qs,function(q) r[q[1]+1,q[2]+1]) }
print(checkIfPrerequisite(3,list(c(1,2),c(1,0),c(2,0)),list(c(1,0),c(1,2))))
