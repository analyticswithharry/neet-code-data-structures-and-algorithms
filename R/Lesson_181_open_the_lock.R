# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 181 -- Open The Lock
# Category   : Graphs
# Difficulty : Medium
# Study Plan : Day 91
# =============================================================
#
# QUESTION:
#   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
# =============================================================
openLock <- function(dead,target){ D<-dead; if("0000"%in%D) return(-1); if(target=="0000") return(0); seen<-"0000"; q<-list(c("0000",0)); while(length(q)>0){ x<-q[[1]]; q[[1]]<-NULL; s<-x[1]; d<-as.integer(x[2]); for(i in 1:4) for(delta in c(-1,1)){ ch<-as.integer(substr(s,i,i)); nc<-(ch+delta+10)%%10; ns<-paste0(substr(s,1,i-1),nc,substr(s,i+1,4)); if(ns==target) return(d+1); if(!(ns%in%seen)&&!(ns%in%D)){ seen<-c(seen,ns); q[[length(q)+1]]<-c(ns,as.character(d+1)) } } }; -1 }
cat(openLock(c("0201","0101","0102","1212","2002"),"0202"),"\n")
