# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 174 -- Surrounded Regions
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 87
# =============================================================
#
# QUESTION:
#   Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).
# =============================================================
solve_regions <- function(b){ R<-length(b); C<-nchar(b[[1]]); m<-do.call(rbind,lapply(b,function(s) strsplit(s,"")[[1]])); dfs<-function(r,c){ if(r<1||r>R||c<1||c>C||m[r,c]!='O') return(); m[r,c]<<-'S'; dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1) }; for(r in 1:R){ dfs(r,1); dfs(r,C) }; for(c in 1:C){ dfs(1,c); dfs(R,c) }; m[m=='O']<-'X'; m[m=='S']<-'O'; apply(m,1,paste,collapse="") }
print(solve_regions(c("XXXX","XOOX","XXOX","XOXX")))
