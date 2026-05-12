# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 090 -- Swim In Rising Water
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 45
# =============================================================
#
# QUESTION:
#   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
# =============================================================

swimInWater <- function(grid){
  n <- nrow(grid); pq <- list(c(grid[1,1],1,1))
  key <- function(r,c) paste(r,c,sep=",")
  seen <- new.env(hash=TRUE); assign(key(1,1), TRUE, envir=seen); ans <- 0
  dr <- c(1,-1,0,0); dc <- c(0,0,1,-1)
  while (length(pq) > 0){
    vs <- sapply(pq, function(x) x[1]); i <- which.min(vs)
    x <- pq[[i]]; pq[[i]] <- NULL; ans <- max(ans, x[1])
    if (x[2]==n && x[3]==n) return(ans)
    for (k in 1:4){
      nr <- x[2]+dr[k]; nc <- x[3]+dc[k]
      if (nr>=1 && nr<=n && nc>=1 && nc<=n && !exists(key(nr,nc), envir=seen, inherits=FALSE)){
        assign(key(nr,nc), TRUE, envir=seen); pq[[length(pq)+1]] <- c(grid[nr,nc],nr,nc)
      }
    }
  }
  -1
}
print(swimInWater(matrix(c(0,1,2,3), nrow=2, byrow=TRUE)))
