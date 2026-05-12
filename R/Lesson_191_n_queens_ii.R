# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 191 -- N Queens II
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 96
# =============================================================
#
# QUESTION:
#   Return number of distinct solutions for n-queens.
# =============================================================
totalNQueens <- function(n){ cnt<-0; c<-c(); d1<-c(); d2<-c(); bt<-function(r){ if(r>n){ cnt<<-cnt+1; return() }; for(i in 1:n){ if((i %in% c)||((r-i)%in%d1)||((r+i)%in%d2)) next; c<<-c(c,i); d1<<-c(d1,r-i); d2<<-c(d2,r+i); bt(r+1); c<<-c[-length(c)]; d1<<-d1[-length(d1)]; d2<<-d2[-length(d2)] } }; bt(1); cnt }
cat(totalNQueens(4),"\n")
