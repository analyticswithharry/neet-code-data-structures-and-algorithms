# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 186 -- Gas Station
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 93
# =============================================================
#
# QUESTION:
#   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
# =============================================================
canCompleteCircuit <- function(g,c){ s<-0; t<-0; tot<-0; for(i in seq_along(g)){ d<-g[i]-c[i]; t<-t+d; tot<-tot+d; if(t<0){ s<-i; t<-0 } }; if(tot<0) -1 else s }
cat(canCompleteCircuit(c(1,2,3,4,5),c(3,4,5,1,2)),"\n")
