# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 162 -- Multiply Strings
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 81
# =============================================================
#
# QUESTION:
#   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
# =============================================================
mul <- function(a,b){ if(a=="0"||b=="0") return("0"); n<-nchar(a); m<-nchar(b); r<-rep(0,n+m); ca<-as.integer(charToRaw(a))-48; cb<-as.integer(charToRaw(b))-48; for(i in n:1) for(j in m:1){ p<-ca[i]*cb[j]; s<-p+r[i+j]; r[i+j]<-s%%10; r[i+j-1]<-r[i+j-1]+s%/%10 }; out<-paste(r,collapse=""); sub("^0+","",out) }
cat(mul("123","456"),"\n")
