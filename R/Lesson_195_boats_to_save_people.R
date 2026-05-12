# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 195 -- Boats to Save People
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 98
# =============================================================
#
# QUESTION:
#   Each boat holds at most 2 people, total weight <= limit. Return min boats.
# =============================================================
numRescueBoats <- function(p,limit){ p<-sort(p); i<-1; j<-length(p); b<-0; while(i<=j){ if(p[i]+p[j]<=limit) i<-i+1; j<-j-1; b<-b+1 }; b }
cat(numRescueBoats(c(3,2,2,1),3),"\n"); cat(numRescueBoats(c(3,5,3,4),5),"\n")
