# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 163 -- Car Fleet
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 82
# =============================================================
#
# QUESTION:
#   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
# =============================================================
carFleet <- function(target,pos,sp){ o<-order(-pos); pos<-pos[o]; sp<-sp[o]; f<-0; lt<-0; for(i in seq_along(pos)){ t<-(target-pos[i])/sp[i]; if(t>lt){ f<-f+1; lt<-t } }; f }
cat(carFleet(12,c(10,8,0,5,3),c(2,4,1,1,3)),"\n")
