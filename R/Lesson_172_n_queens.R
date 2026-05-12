# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 172 -- N Queens
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 86
# =============================================================
#
# QUESTION:
#   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
# =============================================================
totalNQueens <- function(n){ cnt<-0; cols<-c(); d1<-c(); d2<-c(); bt<-function(r){ if(r>n){ cnt<<-cnt+1; return() }; for(c in 1:n){ if((c %in% cols) || ((r-c) %in% d1) || ((r+c) %in% d2)) next; cols<<-c(cols,c); d1<<-c(d1,r-c); d2<<-c(d2,r+c); bt(r+1); cols<<-cols[-length(cols)]; d1<<-d1[-length(d1)]; d2<<-d2[-length(d2)] } }; bt(1); cnt }
cat(totalNQueens(4),"\n")
