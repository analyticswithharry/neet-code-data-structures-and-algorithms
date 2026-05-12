# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 201 -- Longest Increasing Path In a Matrix
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 101
# =============================================================
#
# QUESTION:
#   Find length of the longest strictly-increasing path in a 2D grid.
# =============================================================
longestIncreasingPath <- function(g){ R<-length(g); C<-length(g[[1]]); m<-matrix(0,R,C); dfs<-function(r,c){ if(m[r,c]>0) return(m[r,c]); best<-1; for(d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))){ nr<-r+d[1]; nc<-c+d[2]; if(nr>=1&&nr<=R&&nc>=1&&nc<=C&&g[[nr]][nc]>g[[r]][c]) best<-max(best,1+dfs(nr,nc)) }; m[r,c]<<-best; best }; res<-0; for(r in 1:R) for(c in 1:C) res<-max(res,dfs(r,c)); res }
cat(longestIncreasingPath(list(c(9,9,4),c(6,6,8),c(2,1,1))),"\n")
