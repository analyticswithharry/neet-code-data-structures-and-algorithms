# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 173 -- Pacific Atlantic Water Flow
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 87
# =============================================================
#
# QUESTION:
#   Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).
# =============================================================
pacificAtlantic <- function(h){ R<-length(h); C<-length(h[[1]]); pac<-matrix(FALSE,R,C); atl<-matrix(FALSE,R,C); dfs<-function(r,c,seen){ seen[r,c]<-TRUE; for(d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))){ nr<-r+d[1]; nc<-c+d[2]; if(nr>=1&&nr<=R&&nc>=1&&nc<=C&&!seen[nr,nc]&&h[[nr]][nc]>=h[[r]][c]) seen<-dfs(nr,nc,seen) }; seen }; for(c in 1:C){ pac<-dfs(1,c,pac); atl<-dfs(R,c,atl) }; for(r in 1:R){ pac<-dfs(r,1,pac); atl<-dfs(r,C,atl) }; res<-list(); for(r in 1:R) for(c in 1:C) if(pac[r,c]&&atl[r,c]) res[[length(res)+1]]<-c(r-1,c-1); res }
cat(length(pacificAtlantic(list(c(1,2,2,3,5),c(3,2,3,4,4),c(2,4,5,3,1),c(6,7,1,4,5),c(5,1,1,2,4)))),"\n")
