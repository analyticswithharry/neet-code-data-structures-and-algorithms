# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 208 -- Maximum Frequency Stack
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 104
# =============================================================
#
# QUESTION:
#   Push/pop a stack returning the most-frequent element (ties: most recent).
# =============================================================
FreqStack <- function(){ f<-list(); g<-list(); maxf<-0; push<-function(v){ k<-as.character(v); c<-(if(is.null(f[[k]])) 0 else f[[k]])+1; f[[k]]<<-c; if(c>maxf) maxf<<-c; ck<-as.character(c); g[[ck]]<<-c(g[[ck]],v) }; pop<-function(){ ck<-as.character(maxf); arr<-g[[ck]]; v<-arr[length(arr)]; g[[ck]]<<-arr[-length(arr)]; f[[as.character(v)]]<<-f[[as.character(v)]]-1; if(length(g[[ck]])==0) maxf<<-maxf-1; v }; list(push=push,pop=pop) }
fs<-FreqStack(); for(x in c(5,7,5,7,4,5)) fs$push(x); for(i in 1:4) cat(fs$pop()," "); cat("\n")
