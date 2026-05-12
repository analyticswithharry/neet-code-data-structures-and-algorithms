# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 210 -- Dota2 Senate
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 105
# =============================================================
#
# QUESTION:
#   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
# =============================================================
predictPartyVictory <- function(s){ ch<-strsplit(s,"")[[1]]; n<-length(ch); R<-which(ch=='R')-1; D<-which(ch=='D')-1; while(length(R)>0 && length(D)>0){ r<-R[1]; R<-R[-1]; d<-D[1]; D<-D[-1]; if(r<d) R<-c(R,r+n) else D<-c(D,d+n) }; if(length(R)>0) "Radiant" else "Dire" }
cat(predictPartyVictory("RD"),"\n"); cat(predictPartyVictory("RDD"),"\n")
