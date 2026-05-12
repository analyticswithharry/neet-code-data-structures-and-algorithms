# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 47
# =============================================================
#
# QUESTION:
#   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
# =============================================================

findCriticalAndPseudoCriticalEdges <- function(n, edges){
  E <- lapply(seq_along(edges), function(i) c(edges[[i]], i-1))
  E <- E[order(sapply(E, function(e) e[3]))]
  dsu_new <- function(n) list(p=0:(n-1), r=rep(0,n), cnt=n)
  dsu_f <- function(d,x){ while(d$p[x+1]!=x){ d$p[x+1] <<- d$p[d$p[x+1]+1]; x <- d$p[x+1] }; x }
  dsu_u <- function(d,a,b){
    a <- dsu_f(d,a); b <- dsu_f(d,b); if(a==b) return(list(d=d, ok=FALSE))
    if(d$r[a+1]<d$r[b+1]){ t<-a; a<-b; b<-t }
    d$p[b+1] <- a; if(d$r[a+1]==d$r[b+1]) d$r[a+1] <- d$r[a+1]+1; d$cnt <- d$cnt-1
    list(d=d, ok=TRUE)
  }
  kruskal <- function(skip, force){
    d <- dsu_new(n); w <- 0
    if (force >= 0){ res <- dsu_u(d, E[[force+1]][1], E[[force+1]][2]); if(!res$ok) return(Inf); d <- res$d; w <- w + E[[force+1]][3] }
    for (i in seq_along(E)){ if (i-1 == skip) next; res <- dsu_u(d, E[[i]][1], E[[i]][2]); if(res$ok){ d <- res$d; w <- w + E[[i]][3] } }
    if (d$cnt != 1) return(Inf); w
  }
  base <- kruskal(-1,-1); crit <- c(); pseu <- c()
  for (i in seq_along(E)){
    if (kruskal(i-1,-1) > base) crit <- c(crit, E[[i]][4])
    else if (kruskal(-1,i-1) == base) pseu <- c(pseu, E[[i]][4])
  }
  list(crit, pseu)
}
print(findCriticalAndPseudoCriticalEdges(5, list(c(0,1,1),c(1,2,1),c(2,3,2),c(0,3,2),c(0,4,3),c(3,4,3),c(1,4,6))))
